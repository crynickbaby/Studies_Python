import random
from time import sleep
print(f'{"-=-":=^40}')
print(f'{"VAMOS JOGAR PEDRA, PAPEL OU TESOURA":^40}')
print(f'{"-=-":=^40}')
sleep(1)

print("""[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
escolha = int(input('Qual a sua escolha? '))

jokepc = random.randint(0, 2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
sleep(0.5)
if jokepc == 0:
    print('O computador escolheu PEDRA')
    if escolha == 0:
        print('Empatou!')
    elif escolha == 1:
        print('Você ganhou!')
    elif escolha == 2:
        print('Você perdeu!')
if jokepc == 1:
    print('O computador escolheu PAPEL!')
    if escolha == 0:
        print('Você perdeu!')
    elif escolha == 1:
        print('Empatou!')
    elif escolha == 2:
        print('Você ganhou!')
if jokepc == 2:
    print('O computador escolheu TESOURA!')
    if escolha == 0:
        print('Voce ganhou!')
    elif escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Empatou!')
