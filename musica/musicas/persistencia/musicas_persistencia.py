from typing import Optional
from musicas.persistencia.persistencia_bd import(
    conectar_cliente_mongo,
    acessar_colecao
)

NOME_COLECAO = "musica"


COLECAO_MUSICAS = acessar_colecao(
    conectar_cliente_mongo(), 
    NOME_COLECAO
)

async def pesquisar_todas_musicas():
    lista_musicas = []
    filtro = {}
    cursor = COLECAO_MUSICAS.find(filtro)
    async for musica in cursor:
        lista_musicas.append(musica)
    return lista_musicas

# async def pesquisar_todas_musicas():
#     lista_musicas = []
#     cursor = COLECAO_MUSICAS.find({})
#     async for musica in cursor:
#         lista_musicas.append(musica)
#     return lista_musicas

async def pesquisar_pelo_codigo(codigo) -> Optional[dict]:
    filtro = {"código": codigo}
    musica = await COLECAO_MUSICAS.find_one(filtro)
    return musica
