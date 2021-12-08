
import numpy as n

mA = [[2, 4, 1],[5, 7, 8]]

mB = [[2, 4],[5, 7]]

matrizA = n.array(mA)

[Filas_A, Columnas_A] = matrizA.shape

print("Filas : " +  str(Filas_A))
print("Columnas : " +  str(Columnas_A))


print()

matrizB = n.array(mB)

[Filas_B, Columnas_B] = matrizB.shape

print("Filas : " +  str(Filas_B))
print("Columnas : " +  str(Columnas_B))