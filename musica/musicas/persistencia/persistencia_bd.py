from motor.motor_asyncio import AsyncIOMotorClient
from musicas.configuracoes import carregar_configuracoes

def conectar_cliente_mongo() -> AsyncIOMotorClient:
    configuracao = carregar_configuracoes()
    cliente_mongo = AsyncIOMotorClient(configuracao.BD_URL)
    return cliente_mongo

def acessar_base_de_dados(cliente_mongo: AsyncIOMotorClient):
    return cliente_mongo.get_default_database()

def acessar_colecao(cliente_mongo: AsyncIOMotorClient, nome_colecao:str):
    bd = acessar_base_de_dados(cliente_mongo)
    return bd[nome_colecao]
