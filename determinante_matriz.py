# Importa biblioteca de operações matemáticas
import numpy as np 
from numpy import linalg 

# Escolhe o modelo de matriz
print("Pressione 1 para matriz 1x1.")
print("Pressione 2 para matriz 2x2.")
print("Pressione 3 para matriz 3x3.")
print("Pressione 4 para matriz 4x4.")
print("Pressione 5 para sair.")

num=int(input())

# Matriz 1x1
if num==1:
    A11=float(input("Digite o valor de [A11]: "))

    matrix = np.array([[A11]]) 
    print("Matriz 1x1:") 
    print(matrix) 

    det = np.linalg.det(matrix)

    print("O determinante da matriz 1x1 é: {:.2f}".format(det))

# Matriz 2x2
elif num==2:
    A11=float(input("Digite o valor de [A11]: "))
    A12=float(input("Digite o valor de [A12]: "))
    A21=float(input("Digite o valor de [A21]: "))
    A22=float(input("Digite o valor de [A22]: "))

    matrix = np.array([[A11, A12], [A21, A22]]) 
    print("Matriz 2x2:") 
    print(matrix) 

    det = np.linalg.det(matrix)

    print("O determinante da matriz 2x2 é: {:.2f}".format(det))

# Matriz 3x3
elif num==3:
    A11=float(input("Digite o valor de [A11]: "))
    A12=float(input("Digite o valor de [A12]: "))
    A13=float(input("Digite o valor de [A13]: "))
    A21=float(input("Digite o valor de [A21]: "))
    A22=float(input("Digite o valor de [A22]: "))
    A23=float(input("Digite o valor de [A23]: "))
    A31=float(input("Digite o valor de [A31]: "))
    A32=float(input("Digite o valor de [A32]: "))
    A33=float(input("Digite o valor de [A33]: "))

    matrix = np.array([[A11, A12, A13], [A21, A22, A23], [A31, A32, A33]]) 
    print("Matriz 3x3:") 
    print(matrix) 

    det = np.linalg.det(matrix)

    print("O determinante da matriz 3x3 é: {:.2f}".format(det)) 

# Matriz 4x4    
elif num==4:
    A11=float(input("Digite o valor de [A11]: "))
    A12=float(input("Digite o valor de [A12]: "))
    A13=float(input("Digite o valor de [A13]: "))
    A14=float(input("Digite o valor de [A14]: "))
    A21=float(input("Digite o valor de [A21]: "))
    A22=float(input("Digite o valor de [A22]: "))
    A23=float(input("Digite o valor de [A23]: "))
    A24=float(input("Digite o valor de [A24]: "))
    A31=float(input("Digite o valor de [A31]: "))
    A32=float(input("Digite o valor de [A32]: "))
    A33=float(input("Digite o valor de [A33]: "))
    A34=float(input("Digite o valor de [A34]: "))
    A41=float(input("Digite o valor de [A41]: "))
    A42=float(input("Digite o valor de [A42]: "))
    A43=float(input("Digite o valor de [A43]: "))
    A44=float(input("Digite o valor de [A44]: "))

    matrix = np.array([[A11, A12, A13, A14], [A21, A22, A23, A24], [A31, A32, A33, A34], [A41, A42, A43, A44]]) 
    print("Matriz 4x4:") 
    print(matrix) 

    det = np.linalg.det(matrix)

    print("O determinante da matriz 4x4 é: {:.2f}".format(det))     

elif num==5:
    print("Finalizando programa...")

else:
    print("Valor inválido!") 
     

