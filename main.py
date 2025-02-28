from fastapi import FastAPI
from routes.RoleRoutes import router as role_router

app = FastAPI()

app.include_router(role_router)





# https://localhost:8000


# @app.get("/test/")
# async def test():
#     return {
#         "message":"Hello goodmorning",
#         "status": "success"
#     }


# @app.get("/users/{userId}")

# async def getUsers(userId):
#     return {"message":"Users fetched successfully..","data":f"users found with id ${userId}"}