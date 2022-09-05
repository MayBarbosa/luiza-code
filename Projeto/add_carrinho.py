cart = []
# for i in range(5):
id_user = str(input("Nome: "))
id_produto = str(input("produto: "))
price = float(input("preço: "))
quantity = int(input("quantidade: "))

item = [id_user, id_produto, price, quantity]

def add_item_cart(item1):
    pass

print(f'{item}')

def soma_valor_total_carrinho(sacola):
    soma_total = 0
    for s in sacola:
        soma_total = soma_total + (s[3] * s[2])
    
    return soma_total

def cria_sacola():
    sacola = [item]
    valor = soma_valor_total_carrinho(sacola)
    print(valor)

cria_sacola()