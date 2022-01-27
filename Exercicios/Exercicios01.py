# Código 1

print('Olá mundo!')
nome = input('Qual o seu nome? ')
print('Prazer,', nome)


# Código 2

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('valor: '))
s = n1 + n2 + n3
print(f'A soma entre {n1}, {n3} e {n2} é {s}')

# Código 3

print('Olá, seja bem vindo (a), sou uma calculadora que realiza apenas somas entre dois números!')
msg = input('Qual seu nome? ')
print(f'Olá {msg}, é um prazer te conhecer.')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
s = n1+n2

print(f'O valor da soma de {n1} e {n2} é {s}')
print('Muito obrigado por testar!')

# Código 4

algo = input('Digite algo: ')
print(f'O valor {algo} é do tipo: ', type(algo))
print('É alfabeto: ', algo.isalpha())
print('É um número: ', algo.isnumeric())
print('É caixa baixa: ', algo.islower())
print('É caixa alta: ', algo.isupper())
print('É somente espaços: ', algo.isspace())