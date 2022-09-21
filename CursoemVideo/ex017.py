import math
print('Tendo em vista esse triângulo retângulo')
cop = float(input('Digite o comprimento cateto oposto: '))
cad = float(input('Digite o comprimento cateto adjacente: '))
hip = math.hypot(cop, cad)

print(f'O comprimento da hipotenusa é: {hip:.2f}')
