from sqlite3 import Cursor
from motor.motor_asyncio import AsyncIOMotorClient

async def testar():
    print("teste mongo")

    cliente = AsyncIOMotorClient("mongodb+srv://luizacode:senha@cluster0.orxhwyt.mongodb.net/estudo01?retryWrites=true&w=majority")

    print("conectou? Sim")

    meu_diretorio = cliente.get_default_database()
    print("Mainha pasta: ", meu_diretorio)

    nome_colecao = "estudante"
    conjunto_arquivos = meu_diretorio[nome_colecao]
    print("Minha Coleção: ", conjunto_arquivos)

    # estudante = {
    #     "nome": "Mayara",
    #     "ano": "3º ano EM",
    #     "matricula": 1995
    # }
    # resposta = await conjunto_arquivos.insert_one(estudante)
    # print("Depois de inserir: ", resposta)

    # chave_pesquisa = {
    #     "nome": "Mayara"
    # }

    # estudante = await conjunto_arquivos.find_one(chave_pesquisa)
    # print("Resultado da pesquisa: ", estudante)

    # cursor = conjunto_arquivos.find({})
    # async for estudandte in cursor:
    #     print(">>", estudandte)

    # filtro_atualizar = {
    #     "nome": "Mayara"
    # }
    # o_que_atualizar = {
    #     "$set": {
    #         "nome": "Mayara Barbosa"
    #     }
    # }

    # resultado = await conjunto_arquivos.update_one(filtro_atualizar, o_que_atualizar)
    # print(resultado)

    playlist = meu_diretorio["playlist"]
    musica = await playlist.find_one({"usuario.nome": "mayara b"})
    print("Encontrou? ", musica)
    musica["musicas"].append("12121212")
    musica["tempo_total"] = 100

    await playlist.update_one({"usuario.nome": "mayara b"}), {
        "$set": musica
    }







import asyncio
asyncio.run(testar())


