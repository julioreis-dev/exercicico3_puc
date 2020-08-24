def formatar(frase):
    lista_letra = []
    for letra in frase:
        lista_letra.append(letra.upper())
    return lista_letra


nome = input('Digite o seu nome? ')
impressao = formatar(nome)
for word in impressao:
    print(word)