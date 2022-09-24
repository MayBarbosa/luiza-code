# EXERCÍCIO 1

"""import logging
from typing import Type
import math

logging.basicConfig(level=logging.ERROR, filename="logging_users1.log")

def number_validation(n):
    if n < 0: 
        raise ValueError("O número informado deve ser maior que zero")

def add_number():
    while True:    
        try:
            n = int(input("Insira um número: "))
            number_validation(n)
        except ValueError:
            print("O número informado deve ser maior que zero")
            logging.error("O número informado deve ser maior que zero")
            return
        print(math.sqrt(n))  
       
add_number()
"""

# EXERCÍCIO 2

"""import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users2.log")

def denominador_validation(n):
    if n == 0: 
        raise ZeroDivisionError("Não é possível realizar divisão por zero")

def divisao():
    while True:
        try: 
            m = int(input("Insira o numerador: "))
            n = int(input("Insira o denominador: "))
            r = m/n
            denominador_validation(n)
        except ZeroDivisionError:
            print("Não é possível realizar divisão por zero")
            logging.error("Não é possível realizar divisão por zero")
            return
        
        print(f"O resultado da divisão é {r}") 

divisao()  """     


# EXERCÍCIO 3

"""import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users3.log")

try: 
    number = int(input("Digite um número: "))
    logging.error(number)
    print(f"O número digitado foi: {number}") 
except ValueError:
    print("O tipo de dado deve ser um número")
    logging.error("O tipo de dado deve ser um número")"""


# EXERCÍCIO 4  
"""import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users4.log")

try: 
    number = int(input("Digite um número: "))
    logging.info(number)
    print(f"O número digitado foi: {n}") 
except NameError:
    logging.error("Ajustando variável ao valor")
except ValueError:
    print("Erro nos tipos de dado: deve ser um número")
    logging.error("Erro nos tipos de dado: deve ser um número")"""

# EXERCÍCIO 5
"""import math

print(math.sqrt(n)) 

#Erro: NameError -> variável n não foi declarada"""

# EXERCÍCIO 6

#A saída impressa será Algo deu errado, pois há divergência entre a declaração de variável e a chamada 
# (result != resultado)

"""try:
    number_1 = float(input("Insira um número: "))
    number_2 = float(input("Insira outro número: "))
    result = number_1/number_2
    
    print("Resultado: {.2f}".format(resultado))
except ValueError:
    print("Isso não é um número")
except ZeroDivisionError:
    print("Divisão por zero indeterminada")
except:
    print("Algo deu errado")"""
            

# EXERCÍCIO 7

"""try:
    file = open("file.txt" "r")
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    print("Arquivo não encontrado")"""
    
    
# EXERCÍCIO 8

from asyncore import write


try:
    file = open("file.txt", "w")
    file.write("Exemplo de texto")
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Não foi possível escrever no arquivo")
finally:
    file.close()