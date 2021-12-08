import numpy as n

mA = [[2, 4, 1],[5, 7, 8],[1, 7, 3]]   # 3 x 3

matrizA = n.array(mA)


mA_cuadrada =  matrizA.dot(matrizA)
print(mA_cuadrada)

print()
mA_cubica =  mA_cuadrada.dot(matrizA)
print(mA_cubica)

#Tala2 = T * T
#Tala3 = Tala2 * T
#Tala4 = Tala3 * T
#Tala5 = Tala4 * T
#.
#.
#.
#Tala(n) = Tala(n-1) * T


print()
#mA_ala2 = matrizA**2
#print(mA_ala2)
