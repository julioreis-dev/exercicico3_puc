def formatar(frase):
    lista_letra = []
    for letra in frase:
        lista_letra.append(letra.upper())
    return lista_letra


def informar(lista):
    contar_vogal = 0
    contar_consot = 0
    contar_vazio = 0
    lista_vogal = ['A', 'E', 'I', 'O', 'U']
    for n in lista:
        if n in lista_vogal:
            contar_vogal = contar_vogal + 1
        elif n == ' ':
            contar_vazio = contar_vazio + 1
        else:
            contar_consot = contar_consot + 1
    return contar_vazio, contar_vogal, contar_consot



nome = input('Digite a frase? ')
lista1 = formatar(nome)
result = informar(lista1)
print('A frase tem a seguinte característica:'
      f'\n{result[0]} espaços em branco.'
      f'\n{result[1]} vogais.'
      f'\n{result[2]} consoantes.')
