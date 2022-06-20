# Módulo da constante da gravitação universal (G = 6,67.10-11 N.m2.Kg2)
G = 6.67*pow(10,-11)

# Entra com as informações de massa e distância entre os corpos
m1 = float(input("Digite a massa 1: "))
m2 = float(input("Digite a massa 2: "))
d = float(input("Digite a distância entre os corpos: "))

# Fórmula da gravitação universal de Newton (F = G*(m1*m2/d2))
f = G*(m1*m2)/(pow(d,2))

print(f'A Força F de atração entre as massas tem sua intensidade dada por '
      f'{f}')

