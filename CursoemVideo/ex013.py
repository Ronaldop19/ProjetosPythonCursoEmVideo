sal = float(input('Digite o salário atual do funcionário: R$'))
porc = int(input('Digite quantos porcentos de aumento o funcionário irá receber: '))
novsal = sal + (sal * (porc/100))
print(f'O novo salário do funcionário com {porc:.0f}% de aumento será de R${novsal:.2f}')
