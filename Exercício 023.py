# um numero de 0 a 9999 e mostre a unidade, dezena, centena e milhar

numero = int(input( ' Insira um numero de 0 a 9999: '))
und = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('ANALISANDO O NUMERO {}. \n UNIDADE {} \n DEZENA {} \n CENTENA {} \n MILHAR {}'.format(numero, und, dez, cen, mil))



















