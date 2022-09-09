class Professor:
    def __init__(self,nome, idade, salario, acesso):
        self.nome = nome
        self.idade = idade
        self.__salario = salario
        self.acesso = acesso
    
    def __get_salario(self):
        if self.acesso == "S":
            print(self.__salario)
        else: 
            print("Você não possui acesso para visualizar o salário")

    def get_salario(self):
        self.__get_salario()

Professor1 = Professor("Leo", 28, "1.200","N")

Professor1.get_salario()
