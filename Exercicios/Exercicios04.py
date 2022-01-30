# Contagem de fogos

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
