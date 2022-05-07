# Reajuste Salarial: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input(' Olá, partner. Insira seu atual salario aqui: '))
novoSalario = salario + (salario * 15 / 100)
print('Você teve um aumento de 15%. Seu novo salario passara a ser de R${:.2f}.'.format(novoSalario))

