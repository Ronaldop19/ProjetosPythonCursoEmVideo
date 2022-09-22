import random
a1 = str(input('Digite o primeiro: '))
a2 = str(input('Digite o segundo: '))
a3 = str(input('Digite o terceiro: '))
a4 = str(input('Digite o quarto: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)