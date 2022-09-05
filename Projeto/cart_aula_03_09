cart = []

id_user = str(input("Nome: "))
id_produto = str(input("produto: "))
price = float(input("preço: "))
quantity = int(input("quantidade: "))

item = [id_produto, id_user, price, quantity]

def add_item_cart():
    cart.append(item)
    return cart
    print(cart)

def add_item_cart_by_product(id_produto):
    new_list = [item for item in cart if item[0] == id_produto]
    return new_list[0]
    print(new_list[0])

def get_all_items_cart():
    return cart
