
# USUÁRIOS
# import asyncio

# from src.controllers.users import users_crud
# # from src.controllers.cart import carrinho_crud

# loop = asyncio.new_event_loop()
# loop.run_until_complete(users_crud())


# ENDEREÇOS
import asyncio

from src.controllers.address import address_crud

loop = asyncio.new_event_loop()
loop.run_until_complete(address_crud())


# PRODUTOS1
import asyncio

from src.controllers.products import product_crud

loop = asyncio.new_event_loop()
loop.run_until_complete(product_crud())

