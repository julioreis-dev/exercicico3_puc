def formatar(frase):
    lista_letra = []
    for letra in frase:
        lista_letra.append(letra.upper())
    return lista_letra


nome = input('Digite o seu nome? ')
impressao = formatar(nome)
total_word = len(impressao)
contador = 0
x = ''
for word in range(0, total_word):
    x = x + impressao[word]
    print(x)
