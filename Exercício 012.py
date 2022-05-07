# Calculando Descontos: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o valor do produto?: '))
desconto = preco - (preco * 5 / 100)
print('Preço final do seu produto: Seu produto vai custar R${:.2f}!! Você ganhou 5% de desconto.'.format(desconto))
