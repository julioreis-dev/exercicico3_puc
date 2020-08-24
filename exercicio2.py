def inverter(frase):
    lista_letra = []
    for letra in frase:
        lista_letra.append(letra.upper())
    lista_letra.reverse()
    return lista_letra


nome = input('Digite o seu nome? ')
nome_invertido = inverter(nome)
for word in nome_invertido:
    print(word, end=' ')
