# Valor do cateto oposto
co = float(input('Digite o comprimento do cateto oposto: '))
# Valor do cateto adjacente
ca = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("\n************** Resultado **************\n")

print("O valor da hipotenusa é {:.2f}".format(hipotenusa))