# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

valor_emprestimo = int(input("Qual é o valor que deseja pegar emprestado? ")) 
taxa = float(input("Qual é o valor da taxa de juros mensal? "))
tempo = int(input("Em quantos meses você irá pagar o empreéstimo? ")) 

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

print(f"Ao final do empréstimo, você irá pagar {valor_final}")