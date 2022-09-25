from random import randint
from time import sleep
pc = randint(1, 5)
print('Irei pensar em um número entre 1 e 5, tente adivinhar!')
r = int(input('Digite um número: '))
print('Pensando... Hum...')
sleep(1.5)
print(f'Eu pensei no número... {pc}!!!')
if r == pc:
    print('Parabéns, você ganhou!!')
else:
    print('Eu ganhei!! Hahaha')

