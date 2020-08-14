# for x in range(90, 101):
#     print(x)

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range (1,a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))


# a = int(input('Range de numeros: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print('Numero {} é primo'.format(num))

nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Entre com uma nota válida: '))

# a = 0
#
# while a <= 10:
#     print(a)
#     a += 1