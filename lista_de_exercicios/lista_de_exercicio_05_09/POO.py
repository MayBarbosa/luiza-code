# CLASSE
class Entrega:
    def __init__(self, endereco_destinatario, produto, destinatario, transportadora):
        self.endereco = endereco_destinatario
        self.produto = produto
        self.destinatario = destinatario
        self.transportadora = transportadora

    def endereco_entrega(self):
        return f'O endereço de entrega da encomenda é {self.endereco}'

entrega1 = Entrega('Rua 2, 199', 'Secador de cabelo', 'Maria da Silva', 'GFL')

endereco = entrega1.endereco_entrega()
print ("entrega", endereco)

# HERANÇA

class o_aprendiz:
    def __init__(self, participante, apresentador, nacionalidade, temporada, idade, sexo, ganhador):
        self.participante = participante
        self.apresentador = apresentador
        self.nacionalidade = nacionalidade
        self.temporada = temporada
        self.idade = idade
        self.sexo = sexo
        self.ganhador = ganhador

    def get_participante(self):
        return f'O nome do participante é',{self.participante}
    
    def get_temporada(self):
        return f'A temporada dele(a) foi', {self.temporada}

class Jessica(o_aprendiz):
    def __init__(self, participante, apresentador, nacionalidade, temporada, idade, sexo, ganhador, gerencias):
       self.gerencias = gerencias
       super().__init__(participante, apresentador, nacionalidade, temporada, idade, sexo, ganhador)

    def get_gerencias(self):
        return f'{self.participante} teve {self.gerencias} gerencia(s) durante o programa'

participante1 = Jessica('Jessica', 'Chatri', 'Venezuela', 'One Championship', '32', 'feminino', 'Sim', '1')
participante = participante1.get_gerencias()
print ("Participante", participante)

#POLIFORFISMO

class trickster:
    def __init__(self):
        pass

    def form_trickster(self):
        return 'Qualquer uma'

class trapaça(trickster):
    def __init__(self, criminoso):
        self.criminoso = criminoso
        super().__init__()

    def form_trickster(self):
        return f'A forma do trickster é {self.criminoso}'

crime_trickster = trapaça("Ladrão")
print(crime_trickster.form_trickster())
