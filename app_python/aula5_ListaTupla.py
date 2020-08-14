lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'arara']

print(lista_animal[1])

for x in lista_animal:
    print(x)

print(sum(lista))
print(min(lista))
print(max(lista))

print(min(lista_animal))
print(max(lista_animal))

if 'lobo' in lista_animal:
    print('achou')
else:
    print('nao existe, acrescentado')
    lista_animal.append('lobo')

#print(lista_animal)

# lista_animal.sort()
# print(lista_animal)
#
# lista_animal.reverse()
# print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# lista_animal.pop(0)
# print(lista_animal)

# lista_animal.remove('gato')
# print(lista_animal)

# nova_lista = lista_animal * 3
#
# print(nova_lista)

#tupla = objeto imutavel
tupla = (1, 10, 12, 14)
print(tupla[0])
print(len(tupla))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)