import math

# 'Dobro, Triplo, Raiz Quadrada: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'
n1 = int(input('Ola! Vamos transformar um numero em dobro,triplo e descobrir a raiz quadrada? Digite um numero aqui: '))
dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 ** (1 / 2)
print(
    'Olhe só!!! O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {:.2f}.'.format(n1, dobro, triplo, raizQuadrada))
