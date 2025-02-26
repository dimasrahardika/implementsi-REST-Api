from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: str

users_db = []
user_counter = 1

@app.get("/users", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User):
    global user_counter
    new_user = {"id": user_counter, "name": user.name, "age": user.age, "email": user.email, "phone": user.phone}
    users_db.append(new_user)
    user_counter += 1
    return new_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

# Jalankan dengan `uvicorn nama_file:app --reload`
