from fastapi import APIRouter
from models.RoleModels import Role,RoleOut
from controllers.RoleController import getAllRoles,addRole,deleteRole,getUserById

router = APIRouter()
@router.get("/roles/")
async def get_roles():
    return await getAllRoles()

@router.post("/role/")
async def post_role(role:Role):
    return await addRole(role)


@router.delete("/role/{roleId}")
async def delete_role(roleId:str):
    return await deleteRole(roleId)

@router.get("/role/{roleId}")
async def get_user_by_id(roleId:str):
    return await getUserById(roleId)