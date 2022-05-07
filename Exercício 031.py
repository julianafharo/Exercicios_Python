#Custo da Viagem: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

d = float(input( ' INSIRA A DISTÂNCIA DA SUA VIAGEM EM KM: '))

if d <= 200:
    print(' O VALOR A PAGAR SERÁ DE R${:.2f}'.format(0.50 * d))
else:
    print('O VALOR A PAGAR SERÁ DE R${:.2f}'.format(0.45 * d))





