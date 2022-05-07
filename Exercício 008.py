# Conversor de Medidas: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Insira uma distância em metros: '))
cm = metros * 100
mm = metros * 1000
print('A medida de {}m corresponde a: {:.0f} centimetros e {:.0f} milimetros.'.format(metros, cm, mm))
