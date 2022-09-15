din = float(input('Quantos reais você gostaria de converter? R$'))
dol = din/5.16
eur = din/5.15
print(f'Com esse valor, você pode comprar:'
      f'\nU${dol:.2f} ou {eur:.2f}€')