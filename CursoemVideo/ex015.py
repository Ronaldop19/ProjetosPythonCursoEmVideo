dias = int(input('Foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros foi rodado? '))
diaria = int(input('Qual o valor da diária? '))
valkm = float(input('Qual o valor por km rodado? R$'))
print(f'O valor a ser pago é de R${(dias*diaria) + km * valkm}')
