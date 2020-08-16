from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))

def trabalhando_com_time():
    horario = time(hour=15,minute=18,second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def trabalhando_com_date_time():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.month)
    tupla = ('Segunda','Terça','Quarta','Quinta','Sexta','Sabado','Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2020, 6, 12, 12, 37, 12)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2020'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida.strftime('%c'))
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_date_time()