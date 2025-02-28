from config.database import role_collection 
from models.RoleModels import Role,RoleOut
from bson import ObjectId

async def getAllRoles():
    roles = await role_collection.find().to_list(100)
    return [RoleOut(**role) for role in roles]

async def addRole(role:Role):
    result = await role_collection.insert_one(role.dict())
    print(result)
    return {"message":"Role added successfully.."}

async def deleteRole(roleId:str):
    result = await role_collection.delete_one({"_id":ObjectId(roleId)})
    return {"message":"Role deleted successfully"}

async def getUserById(roleId:str):
    result = await role_collection.find_one({"_id":ObjectId(roleId)})
    ans = RoleOut(**result)
    return {"message":"User fetched successfully..","ans":ans}