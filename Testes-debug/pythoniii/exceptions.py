from fileinput import filename
import logging
logging.basicConfig(level=logging.ERROR, filename="logs_exemple.log")
# logging.info("meu primeiro log")
# logging.error("meu primeiro log")

from unittest import result

try:
    numerator = int(input("numerador: "))
    denominator = int(input("denominador: "))
    result = numerator / denominator
    print(f'O resultado é {result}')
    logging.info(result)
except ZeroDivisionError:
    logging.error("não é possivel dividir um número por zero")
except (ValueError, TypeError):
    logging.error("Erro do tipo de dado que vc digitou")
except KeyboardInterrupt:
    print("dados não informados")
finally:
    print("obrigada!")
