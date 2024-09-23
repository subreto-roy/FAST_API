from fastapi import FastAPI, status, Path, Query, Body
from enum import Enum
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Annotated

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
#path=http://127.0.0.1:5000/?skip=1&limit=3

# fake_items_db:list[dict[str, str]] = [{"item_name":"1"}, {"item_name":"2"},{"item_name":"3"}]

# @app.get("/")

# async def index(skip:int = 0, limit:int=10):

#     item = fake_items_db[skip:skip + limit]

#     return [item]

#request body



# @app.get('/')

# async def index():
#     pass

#path validation



# @app.get("/products/{product_id}", tags=["Get single product"])


# @app.get("/", tags=["hello"])

# async def get():
#     return {"hello":" world"} 



#multiple parameter and validation


# from pydantic import BaseModel
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder
# from typing import Annotated


# class User(BaseModel):
#     name: str | None = None
#     username: str
#     password:str
#     age: int | None = 20


# @app.put("/{id}", tags=["update user"])

# async def update_user(id: Annotated[int, Path(title="user id", le=100, ge=0)],
#                        query: Annotated[str | None, Query(title="search query")] = None, 
#                        user: User | None =None):
    
#     result ={"user_id": id}

#     if query:
#         result.update({"query":query})

#     if user:
#         result.update({
#             "user": jsonable_encoder(user)
#         })

#     return JSONResponse(content=result, status_code=200)



# @app.get("/")

# async def root_route():
#     return {"hello": "world"}




# pydantic Body - Fields

# class User(BaseModel):
#     name: str | None
#     username: str
#     bio: str | None = Field(
#         title=" user bio describtion",
#         max_length=4000

#     )
#     salary: float = Field(
#         ge=1000
#     )
#     age: int | None= 20

# @app.put("/users/{userId}", tags=["update user"])
# async def update_user(userId: int, user: Annotated[User, Body(embed=True)]):
#     results = {
#         "userId": userId,
#         "user": user
#     }
#     print(results)
#     return results

# @app.get("/", tags=["Health"])
# async def read_root():
#     return {"message": "Hello World"}


# Nested Model

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from model.user import UserModel

app = FastAPI()


@app.put("/", tags=["update profile"])
async def update_user(request_body: UserModel):
    encoded = jsonable_encoder(request_body)
    print(encoded)
    return JSONResponse(content=encoded, status_code=200)


@app.get("/", tags=["Health"])
async def root_route():
    return {"Hello": "Hello World"}

