from fastapi import FastAPI, status
from enum import Enum
from fastapi.responses import JSONResponse


app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get('/user')

# async def user():
#     return {
#         "id": 1,
#         "name": "Subroto",
#         "password":"subroto"
#     }



#path parameter


# class Role(str, Enum):

#     ADMIN ="ADMIN"
#     USER ="USER"


# @app.get("/user/{role}")

# async def user(role:Role):

#     if role is role.ADMIN:

#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
#             "message":"You are a admin"
#         })
#     else:
#         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
#             "message":"You are not a admin"
#         })




# @app.get('/check/{id}')

# async def Error(id):

#     print(id)
#     return JSONResponse(status_code = 200, content={
#         'user':True
#     })



#query_parameter

fake_items_db:list[dict[str, str]] = [{"item_name":"1"}, {"item_name":"2"},{"item_name":"3"}]

@app.get("/")

async def index(skip:int = 0, limit:int=10):

    item = fake_items_db[skip:skip + limit]

    return [item]

