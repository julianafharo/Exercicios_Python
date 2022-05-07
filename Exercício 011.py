#Pintando Parede: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m².


larg = float(input(' Ola, vamos te ajudar a descobrir quantas latas de tinta voce ira precisar. Insira a largura da sua parede em metros: '))
altu = float(input(' Agora insira a altura da sua parede em metros: '))
area = larg * altu
tinta = area / 2
print(' Serão necessarios {}L de tintas para pintar o total de {}m. quadrados.'.format(tinta, area))


