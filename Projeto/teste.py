# id produto, id usuário, preço, quantidade
from ast import Lambda


carts = [['123', '1', 100.00, 2], ['456','1', 899.00, 1]]

new_lista = None
for item in carts:
	# print(item)
	if item[0] == '123':
		new_lista = item
		# new_lista.append(item)

print(new_lista)

new_list = [item for item in carts if item[0] == '123']
print(new_list[0])

def filtra_item(item, product):
	if item[0] == product:
		return item

# n_list = filter(lambda elem: elem[0] == '123', carts)
# print(list(n_list))



