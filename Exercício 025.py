#Procurando uma String Dentro de Outra: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input(' Diga seu nome: ').strip())
print( 'O SEU NOME POSSUI SILVA? RESULTADO {}'.format('SILVA' in nome.upper()))


