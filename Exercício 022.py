#  Programa que leia o nome completo: nome com todas as letras maiusculas, o nome com as letras minusculas, quantidade de letras sem espaços, quantidade de letras no primeiro nome

nome = str(input('Digite seu nome completo ')).strip()
print(nome.upper())
print(nome.lower())
print('A quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
print( 'A quantidade de letras no primeiro nome: {}'.format(nome.find(' ')))
separa = nome.split()
print(' Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))





































