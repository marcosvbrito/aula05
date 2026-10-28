print("teste 5 entradas de nome, prova01, prova02, prova03. e faça media entre as provas e mostre a situação")
for i in range(1,6):
    nome= input(f"{i}º digite o nome do aluno: ")
    prova01 = float(input("digite o numero da prova 01: "))
    prova02 = float(input("digite o numero da prova 02: "))
    prova03 = float(input("digite o numero da prova 03: "))
    media = (prova01 + prova02 + prova03) / 3
    if media >= 7:
        print("situação: aprovado")
    elif media >= 5:
        print("situação: recuperação")
    else:
        print("situação: reprovado")

    print("\n ---resultado---")
    print(f"aluno: {i}")
    print(f"nome: {nome}")
    print(f"prova 1: {prova01}")
    print(f"prova 2: {prova02}")
    print(f"prova 3: {prova03}")
    print(f"media: {media}")
    #print(f"situação: {situação}")
    print(f"\n")