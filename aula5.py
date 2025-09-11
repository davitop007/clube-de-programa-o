import random

opcoes =  ['cara', 'coroa'] 

moedas = random.randint(0, 1)

escolha = input('Escolha cara ou coroa: ')

if escolha == opcoes[moedas]:
    print('você ganhou')
else:
    print('você perdeu')
