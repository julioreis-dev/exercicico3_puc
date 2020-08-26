def converter(dados):
    lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
                   'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                   'Novembro', 'Dezembro']
    dia = dados[0]
    mes = dados[1]
    ano = dados[2]

    return f'A data de hoje é {dia} de {lista_meses[int(mes)-1]} de {ano}.'


data = input('digite a data de hoje:')
lista_data = data.split('/')
data_convertida = converter(lista_data)
print(data_convertida)
