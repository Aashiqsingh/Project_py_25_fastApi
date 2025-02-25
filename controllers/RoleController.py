from config.database import role_collection 
from models.RoleModels import Role,RoleOut
from bson import ObjectId

async def getAllRoles():
    roles = await role_collection.find().to_list(100)
    return [RoleOut(**role) for role in roles]