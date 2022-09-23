from itertools import product
from src.models.products import( 
    create_product,
    get_product,
    delete_product
)
from src.server.database import connect_db, db, disconnect_db

product_collection = db.product_collection

async def product_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
      
    product = {
        "name": "Colchão Inflável",
        "description": "Colchão de casal inflável portátil",
        "price": "149.90",
        "code": "COL123123"
    }
    
    if option == '1':
        # create product
        product = await create_product(
            product_collection,
            product
        )
        print(product)

    elif option == '2':
        # remove product
        query = await get_product(
            product_collection,
            product["id"]
        )

        result = await delete_product(
            product_collection,
            product["id"]
        )

    await disconnect_db()