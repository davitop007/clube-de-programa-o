import random

opcoes =  ['pedra', 'papel', 'tesoura'] 

comp = random.randint(0, 1, 2)

escolha = input('Escolha pedra, papel, tesoura' \
': ')

if escolha == 'papel' and opcoes[comp]== 'pedra'):
    print('você ganhou')
elif (escolha == 'pedra' and opcoes[comp] == 'tesoura'):
    print('você ganhou')
elif(escolha == 'tesoura' and opcoes[comp] == 'papel'):
    print('você ganhou')   