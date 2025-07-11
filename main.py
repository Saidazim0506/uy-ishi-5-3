from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import Field
import uvicorn

app = FastAPI()


users = [
    {"id": 1, "name": "Ali", "email": "ali@example.com", "address": "Toshkent"},
    {"id": 2, "name": "Vali", "email": "vali@example.com", "address": "Farg'ona"},
    {"id": 3, "name": "Dilnoza", "email": "dilnoza@example.com", "address": "Andijon"},
    {"id": 4, "name": "Jamshid", "email": "jamshid@example.com", "address": "Toshkent"},
    {"id": 5, "name": "Zuhra", "email": "zuhra@example.com", "address": "Buxoro"},
]



@app.get("/")
def use() -> dict:
    return {"message": "User API ishga tushdi"}



@app.get("/users/")
def get_all_users() -> list[dict]:
    return users


@app.get("/users/{user_id}/")
def get_user_by_id(user_id: Annotated[int, Path(ge=1)]) -> dict:
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}



@app.get("/users/address/{address}/")
def get_users_by_address(address: str) -> list[dict]:
    result = [user for user in users if user["address"].lower() == address.lower()]
    return result if result else [{"message": "Bu manzilda user topilmadi"}]



@app.post("/users/create/")
def create_user(name: Annotated[int, Path(min=2, max=20)], email: Annotated[str, Field()], address: Annotated[str, Field()]):
    users.append = (
        {
            "id": len(users) + 1,
            "name": name,
            "email": email,
            "address": address
        }
    )
    return {"message": "Yangi user qo'shildi", "user":}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)


