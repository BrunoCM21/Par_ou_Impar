# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random

player = 'par'
pc = 'ímpar'
numero_jogado_player = 0
numero_jogado_pc = 0
contador_wins = 0

while True:
    escolha_player = str(input('Escolha entre Par (p) ou Ímpar (i): ')).upper().strip()[0]

    while escolha_player not in 'PI' and escolha_player != 'PAR' and escolha_player != 'IMPAR' and escolha_player != 'ÍMPAR':
        escolha_player = str(input('Você escreveu um valor inválido, escolha entre Par (p) ou Ímpar (i): ')).upper().strip()

    if escolha_player == 'P' or escolha_player == 'PAR':
        player = 'par'
        pc = 'impar'
    elif escolha_player == 'IMPAR' or escolha_player == 'I':
        player = 'impar'
        pc = 'par'

    numero_jogado_player = int(input('Insira o número que você quer mostrar, sendo menor que 10: '))

    while numero_jogado_player > 10 or numero_jogado_player < 0:
        numero_jogado_player = int(input('Insira um número válido sendo menor que 10: '))

    numero_jogado_pc = random.randint(0, 10)

    soma = numero_jogado_player + numero_jogado_pc

    print('='*60)

    if soma % 2 == 0:
        print(f'A máquina mostrou {numero_jogado_pc} e resultado da {soma}, portanto é par')
        vitoria = 'par'
    else:
        print(f'A máquina mostrou {numero_jogado_pc} e o resultado da {soma}, portanto é ímpar')
        vitoria = 'impar'

    if player == vitoria:
        print('Player venceu!!!')
        contador_wins += 1
        print('=' * 60)
    if pc == vitoria:
        print('Máquina venceu!!!')
        print('=' * 60)
        break


if contador_wins >= 2:
    print(f'PARABÉNS!!! Você ganhou {contador_wins} partidas consecutivas')
elif contador_wins == 1:
    print(f'BOA!!! Você ganhou apenas {contador_wins} partida')
else:
    print(f'Você não ganhou nenhuma partida, perdeu de primeira. HAHAHA')