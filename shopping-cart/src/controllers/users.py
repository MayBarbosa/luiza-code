from src.models.user import (
    create_user,
    get_user_by_email,
    update_user,
    delete_user,
    get_users
)

from src.models.address import(
    get_address_by_user
)
from src.server.database import connect_db, db, disconnect_db


async def users_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    users_collection = db.users_collection
    address_collection = db.address_collection
    users =  {
        "email": "lu_domagalu@gmail.com",
        "password": "213sd312re3",
        "is_active": True,
        "is_admin": False
    }

    if option == '1':
        # create user
        users = await create_user(
            users_collection,
            users
        )
        print(users)
    elif option == '2':
        # get user
        users = await get_user_by_email(
            users_collection,
            users["email"]
        )
        print(users)
    elif option == '3':
        # update
        users = await get_user_by_email(
            users_collection,
            users["email"]
        )

        user_data = {
            "password": 'new_password1234'
        }

        is_updated, numbers_updated = await update_user(
            users_collection,
            users["_id"],
            user_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        users = await get_user_by_email(
            users_collection,
            users["email"]
        )

        result = await delete_user(
            users_collection,
            users["_id"]
        )

        print(result)
    elif option == '5':
        # pagination
        users = await get_users(
            users_collection,
            skip=0,
            limit=2
        )
        print(users)
    
    elif option == '6':
        #busca endereço
        users = await get_address_by_user(
            address_collection,
            users_collection,
            users["address"]
        )


    await disconnect_db()
