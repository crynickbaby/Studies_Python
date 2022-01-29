# Aprovador de empréstimo

from time import sleep


vcasa = float(input('Digite o valor da casa que você quer financiar: '))
vsalario = float(input('DIgite quanto você recebe: '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = (vcasa / anos) / 12
print('Calculando')
sleep(2)
print(f'Em {anos} anos você irá pagar um total de R${prestação:.2f} por mês')
sleep(2)
condição = vsalario * 0.3
if prestação > condição:
    print('-=-'*20)
    print('Você não pode realizar um empréstimo')
    print('-=-'*20)
else:
    print('-=-'*20)
    print('Empréstimo aprovado')
    print('-=-'*20)

# Maior e menor

valor1 = int(input('Digite um valor inteiro: '))
valor2 = int(input('Digite outro valor inteiro: '))
if valor1 > valor2:
    print(f'{valor1} é maior que {valor2}')
elif valor2 > valor1:
    print(f'{valor2} é maior que {valor1}')
else:
    print('Os valores são iguais!')

# Calculadora de médias

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print(f'Sua média foi de {media}. Você está REPROVADO')
elif media >= 7.0:
    print(f'Sua média foi de {media}. Você está APROVADO!')
else:
    print(f'Sua média foi de {media}. Você está de recuperação')

# Classificação

from datetime import date
from time import sleep
ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
print(f'Estamos no ano de {ano}. Você nasceu no ano de {nascimento}. Então você tem {idade} anos!')
sleep(1)
if idade <= 9:
    print('Você é classificado como MIRIM!')
elif idade <= 14:
    print('Você é classificado como INFANTIL!')
elif idade <= 19:
    print('Você é classificado como JUNIOR!')
elif idade == 20:
    print('Voce é classificado como SÊNIOR')
else:
    print('Você é classificado MASTER!')

# Tipos de triângulo

from time import sleep


print('Iremos ler 3 valores de reta e diremos que tipo de triângulo ele é!')
sleep(1)
lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

medida1 = lado1 + lado2
medida2 = lado2 + lado3
medida3 = lado3 + lado1
if medida1 < lado3:
    print('Seu triângulo não pode existir!')
elif medida2 < lado1:
    print('Seu triângulo não pode existir!')
elif medida3 < lado3:
    print('Seu triângulo não pode existir!')

elif lado1 == lado2 == lado3:
    print('Seu triangulo é Equilátero!')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('Seu triângulo é Isósceles')
elif lado1 != lado2 != lado3:
    print('Seu triangulo é Escaleno!')

# IMC

peso = float(input('Qual o seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso / altura**2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso!')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é de {imc:.1f}, você está no peso ideal!')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é de {imc:.1f}, você está acima do peso!')
elif imc > 30 and imc < 40:
    print(f'Seu IMC é de {imc:.1f}, você está com obesidade!')
elif imc >= 40:
    print(f'Você tem OBESIDADE MÓRBIDA!') 

# Opções de pagamento

from time import sleep


produto = float(input('Digite o valor do produto R$ '))
print("""Para as opções de pagamentos escolha:
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO""")
escolha = int(input('Digite o número da sua escolha: '))
sleep(2)
if escolha == 1:
    valor = produto * 0.10
    print(
        f'A vista em dinheiro você possui 10% de desconto. Você irá pagar R${produto - valor:.2f}')
elif escolha == 2:
    valor = produto * 0.05
    print(f'A vista no cartão você tem 5% de desconto. Você irá pagar R${produto - valor:.2f}')
elif escolha == 3:
    print(f'Em até duas vezes no cartão você paga R${produto}')
elif escolha == 4:
    valor = produto * 0.20
    print(f'Em 3x ou mais no cartão você paga R${produto + valor:.2f}') 
