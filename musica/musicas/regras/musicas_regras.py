from musicas.persistencia import musicas_persistencia

async def pesquisar_todas():
    lista = await musicas_persistencia.pesquisar_todas_musicas()
    return lista

async def pesquisar_pelo_codigo(codigo: str):
    musica = await musicas_persistencia.pesquisar_todas_musicas()
    return musica
