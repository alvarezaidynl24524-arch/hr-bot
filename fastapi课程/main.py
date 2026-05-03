import uvicorn
from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import List
app = FastAPI()
# class Item(BaseModel):
#     name: str
#     price: float
#     age:int
#     sex:str="男"
#
#
# @app.post("/item/")
# def read_item(item:Item):
#     return item


@app.get("/items/")
def read_items(q: str = Query( default="zzz",alias="item-query")):
    return {"q": q}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)
