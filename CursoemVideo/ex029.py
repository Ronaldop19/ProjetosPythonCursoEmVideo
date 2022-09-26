v = int(input('Qual a velocidade do carro? '))
m = (v - 80) * 7
if v > 80:
    print('MULTADO! Velocidade permitida excedida.\n'
          f'O valor da multa é de: R${m}')

print('Dirija com segurança, tenha um bom dia!')
