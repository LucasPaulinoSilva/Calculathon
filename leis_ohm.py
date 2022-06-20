# Escolhe qual grandeza elétrica cálcular
print("Pressione 1 para calcular a tensão.")
print("Pressione 2 para calcular a resistência.")
print("Pressione 3 para calcular a corrente.")
print("Pressione 4 para sair.")

num=int(input())

# Cálculo de tensão (Volts)
if num==1:
    print("Calculando tensão:")
    i=float(input("Digite o valor da corrente: "))
    r=float(input("Digite o valor da resistência: "))
    v=i*r
    print("O valor da tensão é =" , v, "V")

# Cálculo de resistência (Ohms)
elif num==2:
    print("Calculando resistência:")
    v=float(input("Digite o valor da tensão: "))
    i=float(input("Digite o valor da corrente: "))
    r=v/i
    print("O valor da resistência é =" , r, "Ω")

# Cálculo de corrente (Ampére)
elif num==3:
    print("Calculando corrente:")
    v=float(input("Digite o valor da tensão: "))
    r=float(input("Digite o valor da resistência: "))
    i=v/r
    print("O valor da corrente é =" , i, "A")    

elif num==4:
    print("Finalizando programa...")

else:
    print("Valor inválido!") 
     






