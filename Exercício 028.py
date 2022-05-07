# Jogo da Adivinhação: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('-=-' *20)
print('Vamos jogar? Vou pensar em um numero entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
j = int(input(' Qual numero eu pensei?'))
print(' PROCESSANDO.......')
sleep(3)
if j == computador:
    print(' UHUUUL, PARABENS! Você venceu!!!!!!')
else:
    print(' GANHEI, HEHEHEHE. Eu pensei no {} '.format(computador))


