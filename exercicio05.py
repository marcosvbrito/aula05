print("teste 5 numeros e verifique se e par ou impar")
for i in range(1,6):
    numero = int(input(f"{i}º numero"))

    if numero % 2 == 0:
        print("o numero e par")
    else:
         print("o numero e impar")