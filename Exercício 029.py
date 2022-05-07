#Radar Eletrônico: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.

v = float(input(' Velocidade: '))
if v > 80:
    print(' MULTADO. Você ultrapassou o limite de velocidade. Será cobrado 7 reais de multa. Valor a pagar {:.2f}R$'.format((v - 80) * 7))
else:
    print(' Parabéns. Você está dentro da velocidade.')

