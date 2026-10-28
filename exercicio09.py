print("menu:")
print("1- par ou impar")
print("2- compare o numero")
print("3- calcule o dobro")
resposta = "sim"
while resposta == "sim":
    opcao = int(input("escolha uma opção: "))
    match opcao:
        case 1:
            print("par ou impar")
            numero = int(input("numer: "))
            if numero %2 == 0:
                print(f"{numero} e par")
            else:
                print(f"{numero} e impar")
        case 2:
            print("compare os numeros")
            n1 = int(input("1º numero: "))
            n2 = int(input("2º numero: "))
            if n1 > n2:
                print(f"{n1} e maior que {n2}")
            elif n1 < n2:
                    print(f"{n1} e menor que {n2}")
            else:
                    print(f"{n1} e igual a {n2}")
        case 3:
            print("dobro")
            num = int(input("escolha um numero: "))
            dobro = num * 2
            print(f"o dobro de {num} e {dobro}")
        case _:
            print("opção ivalida")
    resposta = input("deseja continuar? (sim ou não)")
    if resposta != "sim":
        print("programação encerrdo")
        break