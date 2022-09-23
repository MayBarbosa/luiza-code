import logging
logging.basicConfig(level=logging.ERROR, filename="logs_example.log")
logging.basicConfig(level=logging.INFO, filename="logs_example.log")
users = []
try:
    def user_add():
        name = input("Digite o nome do usuário: ")
        age = input("Digite a idade do usuário: ")
        logging.info(name)
        logging.info(age)
    
        users.append({"name": name, "age": age})
        logging.info(users.append)
    
        print("\nUsuário cadastrado com sucesso!")
    
    def users_list():
        print("\n")
        for user in users:
            print("{} - {} anos".format(user["name"], user["age"]))

    while True:
        option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
        if option == 1:
            user_add()
        elif option == 2:
            users_list()
        elif option == 3:
            exit()
        else:
            print("Opção inválida!")

except (ValueError, TypeError):
    print("Formato inválido, digite o número a opção desejada")
    logging.error("Formato inválido, digite o número a opção desejada")
    