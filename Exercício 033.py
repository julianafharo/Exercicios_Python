# Maior e Menor Valores: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input(' Digite um numero: '))
n2 = int(input( ' Digite outro numero: '))
n3 = int(input( ' E por fim, o ultimo numero: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(' O maior numero da lista é {}'.format(maior))
# menor
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(' O menor numero da lista é {}'. format(menor))









