print("faça uma tabuada com um numero escolhido pelo usuario")
numero= int(input("digite um numero para a tabuada: "))
for i in range(0, 11):
    resultado = numero *i
    print(f"{numero} x {i} = {resultado}")