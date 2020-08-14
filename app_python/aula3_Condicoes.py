a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('o maior número é {}'.format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o maior número é {}'.format(c))

d = int(input('Quarto valor: '))
e = int(input('Quinto valor: '))

resto = d % 2
resto_b = e % 2

if resto == 0 or not resto_b > 0:
    print('Foi digitado um número par')
else:
    print('Só foi digitado número impar')

f = int(input('Primeiro bimestre: '))
if f > 10:
    f = int(input('Você digituou errado. Primeiro bimestre: '))
g = int(input('Segundo bimestre: '))
if g > 10:
    g = int(input('Você digituou errado. Primeiro bimestre: '))
h = int(input('Terceiro bimestre: '))
if h > 10:
    h = int(input('Você digituou errado. Primeiro bimestre: '))
i = int(input('Quarto bimestre: '))
if i > 10:
    i = int(input('Você digituou errado. Primeiro bimestre: '))

media = (f + g + h + i) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media: {}'.format(media))
else:
    print('foi informado alguma nota errada')

print('fim')
