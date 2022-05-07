#Ano Bissexto: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Digite o ano que deseja consultar ou apenas 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano %100 != 0 or ano %400 == 0:
    print('Sim, o ano {} é bisexto'.format(ano))
else:
    print('Não, o ano {} não é bisexto'.format(ano))
