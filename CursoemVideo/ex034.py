sal = float(input('Digite o salário atual: R$'))

if sal > 1250:
    nsal = sal + (sal * 0.1)
else:
    nsal = sal + (sal * 0.15)
print(f'O novo salário é de: R${nsal:.2f}')
