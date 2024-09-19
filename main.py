import pandas as pd
def forca_opcao(msg, conjunto_opcoes, msg_erro = 'Inválido'):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f'{msg}\n {opcoes}\n =>')
    while escolha not in conjunto_opcoes:
        print(msg_erro)
        escolha = input(f'{msg}\n {opcoes}\n =>')
    return escolha


def meu_in (lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i


def forca_numero(msg, msg_erro = 'Inválido'):
    num = input(msg)
    while not (num.isnumeric()):
        print(msg_erro)
        num = input(msg)
    return int(num)

'''
escolha = forca_opcao('Qual carro você quer ver?', carros['modelo'])
index = meu_in(carros['modelo'], escolha)
'''
carros = {
    'modelo': ['opala', 'marea', 'kombi', 'celtinha', 'uno', 'up', 'monza', 'corcel'],
    'potência (cv)':[172, 130, 250, 140, 100, 120, 150],
    'consumo (km/l)': [1, 3, 8, 7, 15, 2, 1.5],
    'cor': ['laranja', 'verde', 'branco', 'preto', 'prata', 'azul'],
    'ano': ['1972', '2004', '1985', '2014', '2001', '1980', '1975'],
    'estoque' : [5,6,7,8,9,10,11],
    'preço(R$)': [50, 10, 2.5, 1000000, 100, 200, 999999]
}

s_ou_n = ['sim', 'não']
carros_novo = {}
carrinho = {
    'Carros': {},
    'Valor Total': 0,
    'Endereço': {
        'Rua': '',
        'CEP': '',
        'Número': ''
    }
}
for index in range(len(carros['modelo'])):
    nome = carros['modelo'][index]
    carros_novo[nome] = index

while True:
    escolha = forca_opcao('Qual carro você quer ver?', carros['modelo'])
    index_escolha = carros_novo[escolha]
    for key in carros.keys():
        print(key, carros[key][index_escolha])
    comprar = forca_opcao('Você vai comprar? \n--> ', s_ou_n)
    if comprar == s_ou_n[0]:
        qtd = forca_numero(f'Quantos {escolha}? ')
        if carros['estoque'][index_escolha] >= qtd:
            carros['estoque'][index_escolha] -= qtd
            carrinho['Valor Total'] += qtd*carros['preço(R$)'][index_escolha]
            if escolha not in carrinho['Carros'].keys():
                carrinho['Carros'][escolha] = qtd
            else:
                carrinho['Carros'][escolha] += qtd
        else:
            print(f'Não há {qtd} de {escolha} em estoque. Voltaremos ao início. ')
            continue
        encerrar = forca_opcao('Quer encerrar a compra?', s_ou_n)
        if encerrar == s_ou_n[0]:
            for key in carrinho['Endereço'].keys():
                carrinho['Endereço'][key] = input(f'Diga o/a {key}')
            print(carrinho)
            print('Tenho que montar o carrinho do usuário, calma!')
            break
    else:
        ver_mais = forca_opcao('Quer ver outras opções?', s_ou_n)
        if ver_mais == s_ou_n[0]:
            continue
        else:
            break