n1 = int(input("Digite um numero: "))
print(30*"=-")
n2 = int(input("Digite um numero: "))
print(30*"=-")

print(f"Você digitou  {n1} e {n2}")
escolha = int(input('''Qual será a operação que deseja fazer?
          1 = Para somar
          2 = Para subtrair
          3 = para multiplicar
          Opção escolhida: '''))
print(30*"=-")


if escolha == 1:
    print(f'Você escolheu somar: {n1}+{n2} = {n1+n2}')
elif escolha == 2:
    print(f'Você escolheu subtrair: {n1}-{n2} = {n1-n2}')
elif escolha == 3:
    print(f'Você escolheu multiplicar: {n1}*{n2} = {n1*n2}')
else:
    print('Não escolheu nenhuma opção valida:')