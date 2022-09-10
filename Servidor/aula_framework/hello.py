from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

###### Exemplo de Query Parameters ######
dados = [{"1": "A"}, {"2": "B"}, {"3": "C"}]
@app.get("/itens/")
async def ler_item(numero: int = 0):
    return dados[numero]


###### Exemplo de Body Request ######
from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    id: int

@app.post("/elementos/")
async def create_item(item: Item):
    return item.id, item.nome

###### Exemplo de Body Request ######
from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    id: int

@app.post("/elementos/")
async def retornar_item(item: Item):
    return item.id, item.nome
