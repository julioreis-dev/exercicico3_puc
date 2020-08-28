def formatar(**kwargs):
    x = kwargs.get('nm')
    y = kwargs.get('mail')
    z = kwargs.get('fone')
    w = kwargs.get('adress')
    k = kwargs.get('cpl')
    return ('---------------Cadastro do cliente------------------'
          f'\nNome do cliente:{x}'
          f'\nEmail:{y}'
          f'\nTelefone:{z}'
          f'\nEndereço:{w}'
          f'\nComplemento:{k}')


flag = True
while flag:
    nome = input('Digite o nome do cliente:')
    email = input('Digite o email do cliente:')
    tel = input('Digite o telefone do cliente:')
    endereco = input('Digite o endereço do cliente:')
    compl = input('complemento:')
    formulario = formatar(nm=nome, mail=email, fone=tel, adress=endereco, cpl=compl)
    print(formulario)
    cadastrar = input('Deseja cadastrar o cliente?')
    lista_opc = ['s', 'n']
    if cadastrar.lower() in lista_opc:
        if cadastrar == 's':
            print('Cliente cadastrado com sucesso')
            flag = False
        else:
            print('Refazer o cadastro')
