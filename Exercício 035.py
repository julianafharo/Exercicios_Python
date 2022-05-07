#Analisando Triângulo: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input( ' Digite a primeira medida: '))
l2 = float(input( ' Digite a segunda medida: '))
l3 = float(input( ' E por fim, digite a terceira medida: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(' Sim, podemos fazer um triangulo. ')
else:
    print( ' Hmmm, acho que não conseguimos fazer um triangulo.')

