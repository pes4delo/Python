

print("Bem vindo!")


senhasistema = input("Digite a senha:")
while senhasistema != "senha":
    senhasistema = input("Digite a senha:")

while senhasistema == "senha":
    option = 0
    while option !=3:
        print('''    [1] Senhas dos usuarios
    [2] Cadastro de usuarios
    [3] Sair''')
        option = int(input("Qual é sua opção?"))
        if option == 1:
            with open("senhas.txt", "r") as arquivo:
                usrsenha = arquivo.readlines()
                for line in usrsenha:
                    usr = input("Digite o usuário que deseja saber a senha ou digite sair:")
                    if usr in line:
                        print(line)
                    else:
                        print("Usuario não encontrado")
            arquivo.close()
        if option == 2:
            with open("senhas.txt", "a") as arquivo:
                cadastro = input("Digite o Login do usuario que deseja cadastrar, EX: Usuario.Exemplo = SenhaExemplo: ")
                arquivo.write("\n" + cadastro)
            arquivo.close()
        if option == 3:
            print("Sistema fechando...")
            time.sleep(3)
            sys.exit()






