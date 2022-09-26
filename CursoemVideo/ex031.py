d = float(input('Digite a distância de sua viagem: '))

if d > 200:
    print(f'Valor de sua passagem é de R${d * 0.45:.2f}')
else:
    print(f'O valor de sua passagem é de R${d * 0.5:.2f}')
print('Tenha uma boa viagem!')
