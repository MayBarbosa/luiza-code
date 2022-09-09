class Professor:
    def __init__(self,nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__salario = salario
    
    def __get_salario(self):
        print(self.__salario)

    def get_salario(self):
        self.__get_salario()

Professor1 = Professor("Leo", 28, "1.200")

Professor1.get_salario()
