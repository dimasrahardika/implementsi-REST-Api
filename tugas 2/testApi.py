from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model untuk item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Database sementara
items_db = []

# Endpoint GET: Mendapatkan semua item
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

# Endpoint POST: Menambahkan item baru
@app.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# Endpoint DELETE: Menghapus item berdasarkan ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Jalankan dengan `uvicorn nama_file:app --reload`
