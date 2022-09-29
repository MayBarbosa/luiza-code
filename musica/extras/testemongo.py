from motor.motor_asyncio import AsyncIOMotorClient

async def testar_atlas():
    url = "mongodb+srv://maypbarbosa:55145230@luizacode.ddwgqiu.mongodb.net/musicasbd?retryWrites=true&w=majority" #musicasdb nome banco criado na url
    cliente_mongo = AsyncIOMotorClient(url)
    
    bd = cliente_mongo.get_default_database()
    
    colecao_teste01 = bd["teste01"]
    
    await colecao_teste01.insert_one({
        "teste": "Ana Cortez",
        "codigo": 1
    })
    
    print("Pronto!")
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(testar_atlas())
    
    
#não esquecer de instalar o pip install pymongo[srv]
