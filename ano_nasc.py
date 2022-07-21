def calcula_idade():

    while True:

        nome = str(input("Digite seu nome completo:"))

        if nome == '':
            print("Não pode deixar o campo nome em branco.")
            continue
        elif nome.isnumeric():
            print("Digite apenas letras.")
            continue

        ano_nasc = int(input("Digite seu ano de nascimento:"))

        if ano_nasc == '':
            print("Idade não pode ficar em branco.")
            continue
        elif ano_nasc == str:
            print("Idade inválida.")
            continue
        elif ano_nasc < 1922 or ano_nasc >= 2022:
            print("Digite uma idade válida.")
            continue
        else:
            idade_atual = 2022 - ano_nasc
            print(f"Seu nome é {nome} e em 2022 você completará {idade_atual} anos.")
            break


calcula_idade()