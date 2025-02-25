from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME = "25_internship_FastApi"


client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

role_collection = db["roles"]