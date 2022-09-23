from src.models.address import(
    create_address,
    delete_address,
    get_address
)

from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    
    address_collection = db.address_collection
    users_collection = db.users_collection

    
    query = {
        "address": [{
              "street" : "Rua Quarenta e Sete, Numero 3",
              "cep" : "8465312",
              "district" : "São Paulo",
              "city" : "São Paulo",
              "state" : "São Paulo",
              "is_delivery" : True
        }],
        "user" : {
  	          "id" : "6325c0297ac52b6714b23663",
              "email" : "lu_domagalu@gmail.com"
        }
    }
    
    if option == '1':
        # create address
        query = await create_address(
            address_collection,
            query,
            users_collection
        )
        print()

    elif option == '2':
        # cearch address
        query = await get_address(
            address_collection,
            query["id"]
        )

        result = await delete_address(
            users_collection,
            query["id"]
        )    

    elif option == '3':
        # remove address
        query = await get_address(
            address_collection,
            query["id"]
        )

        result = await delete_address(
            users_collection,
            query["id"]
        )

    await disconnect_db()
