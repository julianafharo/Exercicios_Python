#Sorteando um Item na Lista: Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = input(' Primeiro aluno: ')
a2 = input(' Segundo aluno: ')
a3 = input(' Terceiro aluno: ')
a4 = input(' Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print(' O aluno que ira apagar a lousa é {}'. format(sorteado))










