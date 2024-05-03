'''lista = [6,True,'sadwada',[],4.2]

for i in range(len(lista)):
    print(lista[i])
'''

'''a = 1
b = a
b = 2
print(a)

a = [1,2,3]
b = a
b[0] = 5
print(a)'''

'''lista = [6,True,'sadwada',[],4.2]

for i in range(len(lista)):
    #print(f"lista[{i}] = {lista[i]}")
    lista[i] = 1
print(lista)
'''
'''for elem in lista:
    elem = 1
print(lista)'''

'''lista=[]

lista.append(1)
print(lista)
lista.append(111)
print(lista)
lista.append(11)
print(lista)'''

#1- Declare uma lista com 10 numeros. Faça a soma e a media dos numeros loopando
'''lista = [4,2,4,2,4,2,4,2,4,2]
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(f"A soma dos itens da lista é {soma} e a média é {soma/ len(lista)}")'''

#2- Decalre uma lista com 10 numeros. Coloque os pares em uma nova lista e os impares também
'''lista = [2,3,2,3,2,3,2,3,2,3]
pares = []
impares = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append((lista[i]))
print(f"Lista pares {pares} \n"
      f"Lista impares {impares}")'''
