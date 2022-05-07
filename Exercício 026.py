#Primeira e Última Ocorrência de uma String: Faça um programa que leia uma frase pelo teclado e mostre:
#> Quantas vezes aparece a letra "A".
#> Em que posição ela aparece a primeira vez.
#> Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ').upper().strip())
print( ' A LETRA A APARECE {} VEZES NA FRASE'.format(frase.count('A')))
print( 'A PRIMEIRA LETRA A APARECE NA POSIÇÃO {}'.format(frase.find('A')+1))
print( ' A ÚLTIMA LETRA A APARECE NA POSIÇÃO {}'.format(frase.rfind('A')+1))
