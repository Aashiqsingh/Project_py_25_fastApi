from config.database import user_collection 
from models.UserModels import User,UserOut
from bson import ObjectId

async def addUser(user:User):
    result = await user_collection.insert_one(user.dict())
    print(result)
    return {"message":"User added successfully.."}