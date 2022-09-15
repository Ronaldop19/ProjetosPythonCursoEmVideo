prod = float(input('Digite o preço atual do produto: R$'))
desc = int(input('Quantos % de desconto você gostaria de oferecer? '))
desc = desc/100
proddesc = prod - (prod * desc)      #produto com desconto
print(f'O novo valor do produto com {desc*100:.0f}% de desconto é de R${proddesc:.2f}')
