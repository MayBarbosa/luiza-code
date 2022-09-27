from http.client import HTTPException
from fastapi import FastAPI, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
seguranca = HTTPBasic()

def confere_credencial(credencial: HTTPBasicCredentials = Depends(seguranca)):
    usuario = "May"
    senha = "luizacode2"
    
    credencial_usuario = credencial.username
    credencial_senha = credencial.password

    if usuario == credencial_usuario:
        if senha == credencial_senha:
            return usuario
    

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHGORIZED,
        detail="usuario ou senha incorreto",
        headers={"WWW-Authenticate": "Basic"}
    )

@app.get("/auth/basic")
def Basic (usuario:str = Depends(confere_credencial)):
    return "Usuario:", confere_credencial
