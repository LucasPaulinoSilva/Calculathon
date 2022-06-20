# Importa biblioteca de funções matemáticas
import math

# Tempo próprio (Quantos dias se passaram na espaçonove)
dt0 = float(input("\nDigite o tempo decorrido da espaçonave (em dias): "))
# Velocidade da espaçonave (Percentual da velocidade da luz, ex: 99% = 0.99)
u = float(input("\nDigite a velocidade da espaçonave (em unidades de c): "))
# Constante da velocidade da luz (99 792 458 m/s) ou 3,0 X 108 m/s
c = float(3*10**8)

u = u*c

# fator de lorentz (g = gama)
g = 1.0/(math.sqrt(1 - (u**2/c**2)))

# Tempo em dias decorridos na terra
dt = g*dt0

print("\n0 tempo decorrido na terra foi de %.2f dias!\n" %dt)