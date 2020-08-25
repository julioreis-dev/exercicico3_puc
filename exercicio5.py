def formatar(frase):
    lista_letra = []
    for letra in frase:
        lista_letra.append(letra.upper())
    return lista_letra


nome = input('Digite o seu nome? ')
impressao = formatar(nome)
total_word = len(impressao)
flag = True
while flag:
    x = impressao[0:total_word]
    for n in range(0, len(x)):
        print(f'{x[n]}', end=' ')
    print('')
    total_word = total_word - 1
    if total_word == 0:
        flag = False
