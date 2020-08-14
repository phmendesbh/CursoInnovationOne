a = int(input('Entre com o primeiro valor: '))
b = int(input('Agora o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a & b

#print(type(soma))
#soma = str(soma)
#print(type(soma))

# print('soma: ' + str(soma))
# print('soma: {}'.format(soma))
#
print('soma: {som}. '
      '\nsubtracao: {subt} '
      '\nmultiplicacao: {mult} '
       '\ndivisao: {div} '
       '\nresto: {rest}'.format(som=soma, subt=subtracao, mult=multiplicacao, div=divisao, rest=resto))
