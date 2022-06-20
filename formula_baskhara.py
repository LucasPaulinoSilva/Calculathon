# Entrada dos valores a, b e c
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

# Cálculo do delta
delta = (b ** 2) - 4 * a * c

print("\n************** Resultado **************\n")

# Cálculo das raízes
if a == 0:
    print("O valor de a tem que ser diferente de 0")
elif delta < 0:
    print("A equação não possuí raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("A raíz x1 é: {} \nA raíz x2 é: {}".format(x1, x2))

    
