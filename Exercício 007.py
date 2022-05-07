#Média Aritmética: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Ola, aluno(a). \nPor favor, informe sua primeira nota: '))
n2 = float(input('Por favor, informe sua segunda nota: '))
n3 = int(input('Quantos trabalhos de português?: '))
n4 = int(input('E quantos de matematica?: '))
m = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))