cart = []
for i in range(1):
    id_user = str(input("Nome: "))
    id_produto = str(input("produto: "))
    price = float(input("preço: "))
    quantity = int(input("quantidade: "))

item1 = [id_user, id_produto, price, quantity]

def add_item_cart(item1):
    pass

for i in range(1):
    id_user = str(input("Nome: "))
    id_produto = str(input("produto: "))
    price = float(input("preço: "))
    quantity = int(input("quantidade: "))

item2 = [id_user, id_produto, price, quantity]

def add_item_cart(item2):
    pass

print(f'{item1}')

print(f'{item2}')

def soma_valor_total_carrinho(sacola):
    soma_total = 0
    for s in sacola:
        soma_total = soma_total + (s[3] * s[2])
    
    return soma_total

def cria_sacola():
    sacola = [item1, item2]
    valor = soma_valor_total_carrinho(sacola)
    print(valor)

cria_sacola()