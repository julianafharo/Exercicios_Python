#Sorteando uma Ordem na Lista: O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
g1 = input( 'Nome do grupo 1: ')
g2 = input(' Nome do grupo 2: ')
g3 = input(' Nome do grupo 3: ')
g4 = input(' Nome do grupo 4: ')
lista = [g1, g2, g3, g4]
shuffle(lista)
print(' As ordens de apresentação será:')
print(lista)


