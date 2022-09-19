

from ast import Delete, Return
from turtle import clear
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

OK = "OK"
FALHA = "FALHA"
BEMVINDO = "Seja bem vindo!"

USUARIOS = []
PRODUTOS = []
CARRINHOS = []


# Classe representando os dados do endereço do cliente
class Endereco(BaseModel):
    id: str
    rua: str
    cep: str
    cidade: str
    estado: str

# Classe representando os dados do cliente
class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    endereco: Optional[List[Endereco]] = []

# Classe representando os dados do produto
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: Optional[float]
    quantidade_de_produtos: int


##### ------ BEM VINDO ------ #####
@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')

##### ------ USUARIOS ------ #####
# Criar um usuário
def persistencia_novo_usuario_salvar(novo_usuario):
    USUARIOS.append(novo_usuario)
    return BEMVINDO, novo_usuario

@app.post("/usuario")
async def criar_usuário(novo_usuario: Usuario):
    print(f"Cadastro de um novo usuário:", novo_usuario.dict())
    novo_usuario = persistencia_novo_usuario_salvar(novo_usuario.dict())
    return novo_usuario

# Pesquisar um usuário por id
def persistencia_pesquisar_usuario_pelo_id(id):
    usuario_procurado1 = None
    for usuario in USUARIOS:
        if usuario["id"] == id:
            usuario_procurado1 = usuario
            return usuario_procurado1, OK
        return FALHA

@app.get("/usuario/{id}")
async def retornar_usuario(id: int):
    print("Consulta de usuário pelo ID: ", id)
    return persistencia_pesquisar_usuario_pelo_id(id)

# Pesquisar um usuário por nome
def persistencia_pesquisar_usuario_pelo_nome(nome):
    usuario_procurado2 = None
    for usuario2 in USUARIOS:
        if usuario2["nome"] == nome:
            usuario_procurado2 = usuario2
            return usuario_procurado2, OK
        return FALHA

@app.get("/usuario-por-nome/{nome}")
async def retornar_usuario_com_nome(nome: str):
    print("Consulta de usuário pelo nome: ", nome)
    return persistencia_pesquisar_usuario_pelo_nome(nome)

# Deleta um usuário por id
def persistencia_deletar_usuario_pelo_id(id):
    for usuario3 in USUARIOS:
        if usuario3["id"] == id:
            del usuario3["id"]
            return OK
        return FALHA

@app.delete("/usuario/{id}")
async def deletar_usuario(id: int):
    return persistencia_deletar_usuario_pelo_id(id)

##### ------ ENDEREÇOS ------ #####
# Salvar um novo Endereco
def persistencia_novo_endereço_salvar(id, endereco_novo):
    for usuario in USUARIOS:
        if usuario["id"] == id:
            usuario["endereco"] = (endereco_novo)
            return OK, usuario
    return "Usuário não localizado", FALHA

@app.post("/usuario/{id}/endereco/")
async def criar_endereço(endereco: Endereco, id: int):
    return persistencia_novo_endereço_salvar(id, endereco.dict())

# Pesquisar o endereço de um usuário
def persistencia_pesquisar_endereco_id(id):
    for usuario in USUARIOS:
        if usuario["id"] == id:
            return usuario["endereco"], OK
        return FALHA

@app.get("/usuario/endereco/{id}/")
async def retornar_usuario(id: int):
    print("Consulta de usuário pelo ID: ", id)
    return persistencia_pesquisar_endereco_id(id)

# Deletar endereco
# NÃO CONSEGUI FAZER FUNCIONAR
def persistencia_deletar_endereco_pelo_id(id, end_del): 
    end_del = None
    for usuario in USUARIOS:
        if usuario["id"] == id:
            end_del = usuario["endereco"]
            del end_del         
            return OK
        return FALHA

@app.delete("/usuario/endereco-del/{id}/")
async def deletar_endereco(id: int, end_del: Endereco):
    return persistencia_deletar_endereco_pelo_id(id, end_del)

##### ------ PRODUTOS ------ #####
# criar produto
@app.post("/produto/")
async def criar_produto(novo_produto:Produto):
    PRODUTOS.append(novo_produto)
    return novo_produto, OK

#deletar produto
#NÃO CONSEGUI FAZER FUNCIONAR
def persistencia_deletar_produto_pelo_id(id, prod_del: Produto):#VERIFICAR
    prod_del = None
    for produto1 in PRODUTOS:
        if produto1["id"] == id:
            produto1 = prod_del
            del prod_del
            return OK
        return FALHA

@app.delete("/produto-del/{id}/")
async def deletar_produto(id: int, prod_del: Produto):
    return persistencia_deletar_produto_pelo_id(id, prod_del)

##### ------ CARRINHO ------ #####
#NÃO CONSEGUI FAZER FUNCIONAR
#Criar carrinho
def persistencia_adicionar_carrinho(novo_carrinho, id_usuario, id_produtos):
    novo_carrinho = None
    for usuario in USUARIOS:
        if usuario["id"] == id_usuario:
            for produtos in PRODUTOS:
                if produtos["id"] == id_produtos:
                    CARRINHOS.append(novo_carrinho)
                    return novo_carrinho, OK
                FALHA
            FALHA
        FALHA
    FALHA


@app.post("/carrinho/")
async def adicionar_carrinho(novo_carrinho: CarrinhoDeCompras):
    novo_carrinho = persistencia_adicionar_carrinho(novo_carrinho)
    return novo_carrinho

#Consulta de carrinho
def persistencia_pesquisar_carrinho_id(id):
    for usuario in CARRINHOS:
        if usuario["id"] == id:
            return usuario, OK
        return FALHA

@app.get("/carrinho-buscar/{id}")
async def retornar_carrinho(id: int):
    return persistencia_pesquisar_carrinho_id(id)


#Consulta de carrinho com valor total
@app.get("/carrinho/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    numero_itens, valor_total = 0
    return numero_itens, valor_total


#Deletar carrinho
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    return OK

