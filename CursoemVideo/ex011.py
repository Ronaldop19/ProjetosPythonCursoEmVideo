x = float(input('Qual a largura da parede? '))
y = float(input('Qual a altura da parede? '))
area = x * y
print(f'A dimensão da sua parede é de {x} x {y} e sua área é de {area:.3f}m².    ')
tinta = float(input('Com a tinta que você possui, quantos m² você consegue pintar '
                    'com 1L? '))
qtinta = area / tinta
print(f'Você irá precisar de {qtinta}L de tinta para pintar a sua parede.')
