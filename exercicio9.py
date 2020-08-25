def formatar(num):
    lista_numero = []
    for n in num:
        lista_numero.append(n)
    return lista_numero


def converter_extenso(lista):
    dezena = {2: 'vinte', 3: 'trinta', 4: 'quarenta', 5: 'cinquenta',
              6: 'sessenta', 7: 'setenta', 8: 'oitenta', 9: 'noventa'}
    unidade = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    if int(lista[0]) == 1:
        especiais = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                     'dezesete', 'dezoito', 'dezenove']
        uni_esp = int(lista[1])
        return especiais[uni_esp]
    if lista[0] != 1:
        index = int(lista[0])
        dezn = dezena[index]
        und = int(lista[1])
        if und == 0:
            return dezn
        else:
            return f'{dezn} e {unidade[int(und)-1]}'


numero = input('Digite um numero')
lista_num = formatar(numero)
conversao = converter_extenso(lista_num)
print(conversao)
