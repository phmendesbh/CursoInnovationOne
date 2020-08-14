# conjunto = {1, 2, 3, 4}
# print(type(conjunto))
# print(conjunto)
# conjunto = {1, 2, 3, 4, 4, 2}
# print(conjunto)
# conjunto.add(5)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('uniao: {}'.format(conjunto_uniao))
conjunto_intersecao = conjunto.intersection(conjunto2)
print('intersecao: {}'.format(conjunto_intersecao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('diferenca: {}'.format(conjunto_diferenca))
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferenca2: {}'.format(conjunto_diferenca2))
conjunto_difsimetrica = conjunto.symmetric_difference(conjunto2)
print('diferenca simetrica: {}'.format(conjunto_difsimetrica))


conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))

lista = ['Cachorro', 'Cachorro', 'Gato', 'Gato', 'Elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

conjuntoa = {10, 20, 30, 40, 50}
conjuntoa.discard(40)
print(conjuntoa)
conjuntoa.remove(20)
print(conjuntoa)
