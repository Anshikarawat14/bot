from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid
import random
import time

client = QdrantClient(
    url="Paste_API",
    api_key="...."
)

products = [
    # ----- Men -----
    {
        "name": "Men's Blue Jeans",
        "price": 499,
        "avg_rating": 4.3,
        "ratingCount": 120,
        "img": "https://i5.walmartimages.com/asr/e7ab2fce-65e9-4625-8f1e-c4905b2215c7_1.8d25c00cb88db4b4b125a9c82612447e.jpeg",
        "colour": "Blue",
        "Individual_category": "Jeans",
        "Category": "Bottomwear",
        "category_by_Gender": "Men"
    },
    {
        "name": "Men's Black Shirt",
        "price": 799,
        "avg_rating": 4.5,
        "ratingCount": 230,
        "img": "https://via.placeholder.com/150x200?text=Black+Shirt",
        "colour": "Black",
        "Individual_category": "Shirt",
        "Category": "Topwear",
        "category_by_Gender": "Men"
    },
    {
        "name": "Men's Sneakers",
        "price": 999,
        "avg_rating": 4.6,
        "ratingCount": 340,
        "img": "https://via.placeholder.com/150x200?text=Sneakers",
        "colour": "White",
        "Individual_category": "Shoes",
        "Category": "Footwear",
        "category_by_Gender": "Men"
    },

    # ----- Women -----
    {
        "name": "Women's Red Dress",
        "price": 1299,
        "avg_rating": 4.8,
        "ratingCount": 500,
        "img": "https://via.placeholder.com/150x200?text=Red+Dress",
        "colour": "Red",
        "Individual_category": "Dress",
        "Category": "One Piece",
        "category_by_Gender": "Women"
    },
    {
        "name": "Women's Handbag",
        "price": 799,
        "avg_rating": 4.7,
        "ratingCount": 150,
        "img": "https://via.placeholder.com/150x200?text=Handbag",
        "colour": "Black",
        "Individual_category": "Bag",
        "Category": "Accessory",
        "category_by_Gender": "Women"
    },
    {
        "name": "Women's Flats",
        "price": 699,
        "avg_rating": 4.2,
        "ratingCount": 89,
        "img": "https://via.placeholder.com/150x200?text=Flats",
        "colour": "Beige",
        "Individual_category": "Footwear",
        "Category": "Footwear",
        "category_by_Gender": "Women"
    },

    # ----- Kids -----
    {
        "name": "Kids Yellow T-Shirt",
        "price": 299,
        "avg_rating": 4.6,
        "ratingCount": 80,
        "img": "https://via.placeholder.com/150x200?text=Kids+Tshirt",
        "colour": "Yellow",
        "Individual_category": "T-Shirt",
        "Category": "Topwear",
        "category_by_Gender": "Kids"
    },
    {
        "name": "Kids Blue Jeans",
        "price": 399,
        "avg_rating": 4.4,
        "ratingCount": 90,
        "img": "https://via.placeholder.com/150x200?text=Kids+Jeans",
        "colour": "Blue",
        "Individual_category": "Jeans",
        "Category": "Bottomwear",
        "category_by_Gender": "Kids"
    },
    {
        "name": "Kids Sandals",
        "price": 350,
        "avg_rating": 4.3,
        "ratingCount": 100,
        "img": "https://via.placeholder.com/150x200?text=Kids+Sandals",
        "colour": "Brown",
        "Individual_category": "Footwear",
        "Category": "Footwear",
        "category_by_Gender": "Kids"
    },

    # ----- Accessories -----
    {
        "name": "Leather Belt",
        "price": 499,
        "avg_rating": 4.1,
        "ratingCount": 110,
        "img": "https://via.placeholder.com/150x200?text=Belt",
        "colour": "Brown",
        "Individual_category": "Belt",
        "Category": "Accessory",
        "category_by_Gender": "Men"
    },
    {
        "name": "Women’s Sunglasses",
        "price": 599,
        "avg_rating": 4.9,
        "ratingCount": 210,
        "img": "https://via.placeholder.com/150x200?text=Sunglasses",
        "colour": "Black",
        "Individual_category": "Sunglasses",
        "Category": "Accessory",
        "category_by_Gender": "Women"
    },
    {
        "name": "Kids Cap",
        "price": 199,
        "avg_rating": 4.0,
        "ratingCount": 70,
        "img": "https://via.placeholder.com/150x200?text=Kids+Cap",
        "colour": "Green",
        "Individual_category": "Cap",
        "Category": "Accessory",
        "category_by_Gender": "Kids"
    }
]

# Vector generator
def random_vector(size=1536):
    return [random.random() for _ in range(size)]

# Upload in batches
batch_size = 5
for i in range(0, len(products), batch_size):
    batch = products[i:i + batch_size]
    points = [
        models.PointStruct(
            id=str(uuid.uuid4()),
            vector=random_vector(),
            payload=product
        )
        for product in batch
    ]
    try:
        client.upsert(collection_name="my_collection", points=points)
        print(f"✅ Uploaded batch {i} to {i + len(batch) - 1}")
    except Exception as e:
        print(f"❌ Failed to upload batch {i} to {i + len(batch) - 1}:", e)
    time.sleep(0.5)
