# Média 

nota = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
print(f'Sua média é {(nota + nota2) / 2:.1f}')

# Conversor de medidas

print('Olá,\nSeja bem vindo ao conversor de medidas! ')
m1 = float(input('Primeiro digite o seu valor em metros: '))
km = m1 * 0.001
hm = m1 * 0.01
dam = m1 * 0.1
m = m1
cm = m1 * 100
mm = m1 * 1000
print(f'Km = {km}\nhm = {hm}\ndam = {dam}\nm = {m:.0f}\ncm = {cm:.0f}\nmm = {mm:.0f}')

# Tabuada v1

n = int(input('Digite um valor e iremos mostrar a tabuáda: '))
print(f'{n} x  0 = {n * 0:2}\n{n} x  1 = {n * 1:2}\n{n} x  2 = {n * 2:2}\n{n} x  3 = {n *3:2}\n{n} x  4 = {n * 4:2}\n{n} x  5 = {n * 5:2}\n{n} x  6 = {n * 6:2}\n{n} x  7 = {n * 7:2}\n{n} x  8 = {n * 8:2}\n{n} x  9 = {n * 9:2}\n{n} x 10 = {n * 10}')


# Calculadora de desconto

valor = float(input('Qual o valor da peça? '))
desconto = float(input('Quantos porcentos de desconto? '))
print(f'A peça custava {valor:.2f}, agora custa {valor * (desconto / 100):.2f}')


# Aluguel de carros

dias = int(input('Por quantos dias você alugou? '))
km = int(input('Quantos km você rodou? '))
valor = (dias * 60) + (km * 0.15)
print(f'Você precisa pagar um total de R${valor:.2f}')

# Raiz quadrada

numero = int(input('Digite um numero: '))
raiz = math.sqrt(numero)
print(f'A raiz do numero {numero} é {raiz:.1f}')

# Calculadora de hipotenusa

import math
import emoji
catetooposto = float(input(emoji.emojize('Olá sou sua calculadora de hipotenusa :sunglasses:\nPrimeiro digite o cateto oposto: ', use_aliases=True)))
catetoadjacente = float(input('Agora digite o cateto adijacente: '))
print(f'Aqui está o valor da sua hipotenusa: {math.hypot(catetooposto, catetoadjacente):.2f}')

# Sorteador de alunos

from random import shuffle
nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
sorteio = [nome1, nome2, nome3]
shuffle(sorteio)
print('Os escolhidos foram:')
print(sorteio)

# Seno, cosseno e tangente

from math import radians, sin, cos, tan
angulo = int(input('Olá, digite o seu ângulo que iremos falar o seno, cosseno e tangente: '))
angulo2 = radians(angulo)
print(f'O seno é {sin(angulo2):.2f}°\nCosseno é {cos(angulo2):.2f}°\nTangente é {tan(angulo2):.2f}°')

# Variáveis de nome

nome = input('Olá, digite seu nome aqui: ')
print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
separado = nome.split()
junto = ''.join(separado)
print(f'Seu nome tem um total de {len(junto)} caracteres sem contar com espaços\nCom os espaços ele possui um total de {len(nome)} caracteres')
print(f'Seu primeiro nome tem: {len(separado [0])}')


# Detector de "Santo"

cidade = str(input('Digite o nome da sua cidade e iremos dizer se ela começa ou não com santo: '))
cidade2 = cidade.upper().split()
santo = 'SANTO' in cidade2
print(f'Sua cidade tem o nome de {cidade} e ela começa com Santo? {santo} ')

# Variáveis de nome 2

nome = str(input('Digita seu nome: ')).strip()
lista = nome.split()
print(f'Seu nome é: {lista}')
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[-1]}')

# Adivinhação v1

import random
numero = random.randint(0, 5)
escolha = int(input('Olá, seja bem vindo ao adivinhador de números, tente acertar o número que a máquina pensou de 0 a 5\nEm qual pensou?  '))
if escolha == numero:
    print(f'Parabéns, você acertou. O número escolhido foi: {numero}')
else:
    print('Você errou, tente novamente!')

# Detector de números ímpares e pares

numero = int(input('Digite seu número e iremos mostrar se ele é impar ou par: '))
if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é impar!') 

# Custo de passagem

km = int(input('Quantos Km você vai viajar? '))
if km > 200:
    valor = float(km * 0.45)
    print(f'Sua passagem custa: R$ {valor:.2f}')
else:
    valor2 = float(km * 0.50)
    print(f'Sua passagem custa: R$ {valor2}')


# Triângulos

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 > l2 and l1 > l3:
    medida = l2 + l3
    if medida >= l1:
        print('Seu triângulo existe')
    else:
        print('Seu triângulo não existe')
if l2 > l1 and l2 > l3:
    medida = l1 + l3
    if medida >= l2:
        print('Seu triângulo existe')
    else:
        print('Seu triângulo não existe')
if l3 > l1 and l3 > l2:
    medida = l1 + l2
    if medida >= l3:
        print('Seu triângulo existe')
    else:
        print('Seu triângulo não existe')
if l1 == l2 == l3:
    print('Seu triângulo existe')