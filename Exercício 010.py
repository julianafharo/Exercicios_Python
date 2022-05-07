#Conversor de Moedas: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

n1 = float(input('Saldo disponivel R$: '))
n2 = float(input('Insira a cotação do dolar: '))
a = n1 / n2
print('Seu saldo disponivel equivale a {:.2f} $ sem taxas adicionais de IOF.'.format(a))
taxas = input(' Deseja calcular as taxas? Caso sim, aperte qualquer tecla para continuar ')
b = n1 * 0.068 #IOF
c = n1 + b
print('O total a pagar è {:.2f} R$. Seu saldo em dolar será {:.2f}'.format(c, a))

