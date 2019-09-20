import math

# escolher até onde se quer verificar a existencia de números primos
a = 10

# criar a lista de números primos
listaP = [2]

# verificar se i é primo
for i in range(2,a+1):

    contador = 0

    for j in range(0,len(listaP)):

        if(i % listaP[j] == 0):
            break

        listaP.append(i)

# imprimir lista
for i in range(0,len(listaP)):
    print(listaP[i])
