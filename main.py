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
    print(product)
    query = (product.Name, product.Category, product.Quantity,product.PriceUnity)
    connection.execute(f"Insert into Produto(Name,Category,Quantity,PriceUnity) Values(?,?,?,?)", query)
    connection.commit()
    return {
        "products": [product]
    }

@app.get("/api/products")
async def getProducts():
    produtos = connection.execute("Select * from Produto").fetchall()
    return [dict(x) for x in produtos]

@app.delete("/api/products")
async def deleteProducts(Nome:str):
    connection.execute("delete from Produto where Name = ?",(Nome,))
    connection.commit()
    return{"Message": f"{Nome} deletado com sucesso!"}