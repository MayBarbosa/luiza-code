import requests

def acessa_google():
    try:
        requests.get("https://www.google.com.br")
        return "Google acessado!"
    except Exception:
        return "Não foi possível acessar o Google"
