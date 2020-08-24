def medir(frase):
    cpr = len(frase)
    return cpr


def avaliar(*args):
    if args[0] == args[1]:
        return 'As duas strings são do mesmo tamanho.'
    else:
        return 'As duas strings são de tamanho distintos.'


def avaliar_strings(*args):
    if args[0] == args[1]:
        return 'As duas strings possuem os mesmos conteúdos.'
    else:
        return 'As duas strings possuem conteúdos distintos.'


strg1 = input('Digite aqui a sua primeira string?')
strg2 = input('Digite aqui a sua segunda string?')
valor_cpr1 = medir(strg1)
valor_cpr2 = medir(strg2)
avaliacao = avaliar(valor_cpr1, valor_cpr2)
conteudo = avaliar_strings(strg1, strg2)
print(f'Tamanho de "{strg1}": {valor_cpr1} caracteres'
      f'\nTamanho de "{strg2}": {valor_cpr2} caracteres'
      f'\n{avaliacao}'
      f'\n{conteudo}')
