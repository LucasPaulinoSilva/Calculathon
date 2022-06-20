# Fórmula para cálculo da distância percorrida

V0 = float(input("Digite a velocidade inicial: "))
V = float(input("Digite a velocidade final: "))
Delta_s = float(input("Digite a distância percorrida: ")) 

V0 = V0 / 3.6
V = V / 3.6

S = (V**2 - V0**2) / (2*Delta_s)

print("\n************** Resultado **************\n")

print("A aceleração no trecho é de {:.2f}".format(S), "m/s²")
