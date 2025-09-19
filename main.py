from gemini.gemini import conversa
from Classes.Input import Input
from Classes.Product import Product
from database import base

import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row
app = FastAPI()

origins =[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/gemini")
async def root():
    """
        Utilize isto para testes!
    """
    return {"message":"Conexão estabelecido com sucesso!"}


@app.post("/api/gemini")
async def chatBot(text:Input):
    """
        Use este método para utilizar no chat!
    """
    return {
        "ClientMessage": text.message,
        "GeminiBot":conversa(text.message)
        }


@app.post("/api/products")
async def registerProducts(product:Product):
    try:
        print(product)
        query = (product.name,product.image, product.category, product.quantity,product.price)
        result = connection.execute(f"Insert into Produto(name,image,category,quantity,price) Values(?,?,?,?,?)", query)
        connection.commit()
        return {"message":"Produto Cadastrado!"}
    except NameError:
       print(NameError)

@app.get("/api/products")
async def getProducts():
    produtos = connection.execute("Select id,name,image,category,quantity,printf('%.2f',price) as price from Produto").fetchall()
    return [dict(x) for x in produtos]

@app.delete("/api/products")
async def deleteProducts(Nome:str):
    connection.execute("delete from Produto where name = ?",(Nome,))
    connection.commit()
    return{"Message": f"{Nome} deletado com sucesso!"}

@app.put("/api/products")
async def putProducts():
    return {}