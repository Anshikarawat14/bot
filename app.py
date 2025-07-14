from src.searcher import search_collection
from src.extractor import extractor
from src.parser import parser
from config import TEMPERATURE, GROQ_API_KEY, MODEL_NAME
from flask import Flask, request, jsonify, render_template
from langchain_groq import ChatGroq
import random

app = Flask(__name__, static_folder='static', template_folder='templates')

llm = ChatGroq(
    temperature=TEMPERATURE,
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot')
def chatbot():
    return render_template('index.html')

@app.route('/jeans')
def jeans_page():
    return render_template('jeans.html')

@app.route('/kurtis')
def kurtis_page():
    return render_template('kurtis.html')

@app.route('/skirts')
def skirts_page():
    return render_template('skirts.html')

@app.route('/jumpsuits')
def jumpsuits_page():
    return render_template('jumpsuits.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.json
        conversation_history = data.get('query', '')

        print("👉 User Query:", conversation_history)

        extracted_response = extractor(llm, conversation_history)
        print("🧠 Extracted Response:", extracted_response)

        parsed_data = parser(extracted_response)

        # ✅ Mapping LLM values to your actual DB values
        category_mapping = {
            "Western": "Bottomwear",
            "Indian Wear": "Ethnicwear",
            "Sports Wear": "Activewear",
            "Inner Wear & Sleep Wear": "Loungewear"
            # Add more mappings as needed
        }

        individual_category_mapping = {
            "jeans": "Jeans",
            "tops": "Tops",
            "kurtas": "Kurtas",
            "trousers": "Trousers"
            # Add more as needed
        }

        # ✅ Normalize extracted values
        parsed_data["Category"] = category_mapping.get(parsed_data["Category"], parsed_data["Category"])
        parsed_data["Individual_category"] = individual_category_mapping.get(
            parsed_data["Individual_category"].lower(), parsed_data["Individual_category"]
        )

        print("🧩 Parsed Data:", parsed_data)

        if parsed_data["MOVE_ON"]:
            results = search_collection(
                colour=parsed_data["colour"],
                individual_category=parsed_data["Individual_category"],
                category=parsed_data["Category"],
                category_by_gender=parsed_data["category_by_Gender"]
            )
            return jsonify({"results": results, "message": "Search results for your query"})
        else:
            return jsonify({"results": [], "message": parsed_data["FOLLOW_UP_MESSAGE"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
