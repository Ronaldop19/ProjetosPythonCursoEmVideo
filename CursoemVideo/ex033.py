a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O menor número é: {menor:.2f}')

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior número é: {maior:.2f}')
