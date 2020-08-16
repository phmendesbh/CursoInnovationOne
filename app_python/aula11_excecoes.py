lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    divisao = 10/0
    numero = lista[1]
    x = 1
except ZeroDivisionError:
    print('não é possível realizar divisão por zero')
except IndexError:
    print('Erro de índice')
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
    #base exception se colocar no início, a exceção cai nela primeiro
    #https://docs.python.org/3/library/exceptions.html
except:
    print('Erro desconhecido')
else:
    print('Executa quando não tem exceção')
finally:
    print('Sempre executa')
    arquivo.close()
