# Contagem de fogos

from datetime import date
from time import sleep
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('FELIZ ANO NOVO!')

# Tabuáda v2
n = int(input('Digite o valor que você quer ver a tabuada: '))
for c in range(0, 11):
    print(f'{c} x {n} = {c * n}')

# PA

n = int(input('Qual o primeiro número? '))
r = int(input('Qual a razão? '))
n2 = (n + ((10 - 1) * r)) + r
for pa in range(n, n2, r):
    print(pa)

# Números primos

numero = int(
    input('Digite um número e vamos dizer se ele é um número primo ou não: '))
if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
    print('Seu número não é primo!')
else:
    print('Seu número é primo')

# Detector de palíndromos

frase = str(input('Digite sua frase: ')).strip()
trazprafrente = frase[::-1]
fcort = frase.upper().replace(' ', '')
ftras = fcort[::-1]
print(
    f'A frase \033[032m{frase}\033[m de traz para frente é \033[034m {trazprafrente}\033[m')
if ftras == fcort:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')

# Maiores de idade


s = 0
m = 0
ano = date.today().year

for c in range(1, 8):
    nasc = int(input(f'Digite o ano que a {c}ª pessoa nasceu: '))
    maioridade = ano - nasc
    if maioridade >= 21:
        s += 1
    elif maioridade < 21:
        m += 1
print(f'Há \033[032m{s}\033[m pessoas que já são maior de idade e \033[033m{m}\033[m pessoas que não são maior de idade!')

# Listagem de pessoas

sidades = 0
mvelho = 0
cmulher = 0
maisvelho = []
nomemulher = []
for i in range(1, 5):
    nome = str(input(f'Nome da pessoa número {i}: '))
    idade = int(input(f'Idade da pessoa número {i}: '))
    sexo = int(input(f"""Sexo da pessoa número {i}: 
    [ 4 ] Masculino
    [ 5 ] Feminino
    Sua opção: """))
    sidades = sidades + idade
    if i == 1 and sexo == 4:  # NOME DO MAIS VELHO
        maisvelho = nome
        mvelho = idade
    else:
        if idade > mvelho and sexo == 4:
            maisvelho = nome
            mvelho = idade
    if sexo == 5 and idade < 20:
        cmulher = cmulher + 1
        nomemulher = nome
print(f'A média de idades é: {sidades / 4}')
print(f'O homem mais velho é o {maisvelho} com {mvelho} anos')
print(f'{cmulher} mulher tem menos de 20 anos e é a {nomemulher}!')
