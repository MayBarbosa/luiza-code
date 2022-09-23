"""
# USUÁRIOS
import asyncio

from src.controllers.users import users_crud
# from src.controllers.products import products_crud
# from src.controllers.carrinho import carrinho_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())"""

""""
# ENDEREÇOS
import asyncio

from src.controllers.address import address_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(address_crud())
"""

# PRODUTOS
import asyncio

from src.controllers.products import product_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(product_crud())