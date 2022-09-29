from dotenv import load_dotenv
from pydantic import BaseConfig

class Configuracao(BaseConfig):
    #qual é a URL de conexão do banco de dados.
    bd_url: str

#carrega as variaveis na seguinte forma
#1 - variaveis de ambiente
#2 - Arquivo .env na raiz do projeto

def carregar_configuracoes():
    load_dotenv()
    configuracao = Configuracao()
    return configuracao