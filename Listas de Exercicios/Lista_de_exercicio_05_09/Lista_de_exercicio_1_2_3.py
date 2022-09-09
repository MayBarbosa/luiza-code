class Pessoa:
    def __init__(self,nome, idade, fumante):
        self.nome = nome
        self.idade = idade
        self.fumante = fumante


class PessoaFisica(Pessoa):
   def __init__(self, CPF, nome, idade, fumante):
       super().__init__(nome, idade, fumante)
       self.CPF = CPF

   def getCPF(self):
       return self.CPF

   def setCPF(self, CPF):
       self.CPF = CPF


class PessoaJuridica(Pessoa):
   def __init__(self, CNPJ, nome, idade, fumante):
       super().__init__(nome, idade, fumante)
       self.CNPJ = CNPJ

   def getCPF(self):
       return self.CNPJ

   def setCPF(self, CNPJ):
       self.CNPJ = CNPJ

PessoaPF = PessoaFisica("000.000.000-01", "Vinicius", 28, "F")
PessoaJurid = PessoaJuridica("00.000.000/0001-11", "Leonardo", 28, "F")

print(PessoaPF.nome, PessoaPF.idade)

print(PessoaJurid.fumante)

