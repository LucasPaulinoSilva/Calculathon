# Importa biblioteca de funções matemáticas
import math
 
print("\nLei de Coulomb -> F = k.Q1.Q2/d²")
print("\nDigite 0 na variável que você deseja calcular...\n")
 
F   = float(input("Força F (N) = "))
Q1  = float(input("Carga Q1 (uC) = "))
Q2  = float(input("Carga Q2 (uC) = "))
d   = float(input("Distância d (m) = "))
 
k   = 9.00*10**9

# Cácula Força (N)
if F == 0:
    F = (k*Q1*Q2*10**-12)/d**2
    print("\nF = %.2f N" % F)

# Cálcula carga Q1 (uC)    
elif Q1 == 0:
    Q1 = (F * d**2) / (k*Q2*10**-12)
    print("\nQ1 = %.2f C" % Q1)

# Cálcula carga Q2 (uC)  
elif Q2 == 0:
    Q2 = (F * d**2) / (k*Q1*10**-12)
    print("\nQ2 = %.2f C" % Q2)

# Cálcula distância d (m) ex: 5cm = 00.5
elif d == 0:
    d = math.sqrt(k*Q1*Q2*10**-12/F)
    print("\nd = %.2f m" %d)
else:
    print("\nOpção Inválida!")
 

