from src.models.user import (
    get_user_by_email
)

async def create_address(address_collection, address, users_collection, user):
    try:
        user = await get_user_by_email(users_collection, address.user.email)

        address.user.id = user["id"]

        address = await address_collection.insert_one(address)

    except Exception as e:
        print(f'create_address.error: {e}')


async def get_address(address_collection, address_id):
    try:
        data = await address_collection.find_one({'_id': address_id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_address_by_user(address_collection, address, users_collection):
    try:
        user =  await get_user_by_email(users_collection, address.user.email)
        
        if address.user.email == user["email"]:
            return address

    except Exception as e:
        print(f'get_address_by_user.error: {e}')

async def delete_address(address_collection, address_id):
    try:
        address = await address_collection.delete_one(
            {'_id': address_id}
        )
        if address.deleted_count:
            return {'status': 'Address deleted'}
    except Exception as e:
        print(f'delete_address.error: {e}')
