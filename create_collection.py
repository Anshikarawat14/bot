from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

client = QdrantClient(
    url="Pate_key_here",
    api_key="paste_key"
)

client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

print("✅ Collection recreated successfully.")
