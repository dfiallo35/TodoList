from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Set up the FastAPI app
app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")


# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


# Set up the MongoDB client
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://admin:mongodbadmin@cluster.vhi2i3e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.get("/api/")
async def read_root():
    return {"message": "Hello World"}