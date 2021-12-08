
import numpy as n

mA = [[2, 4, 1],[5, 7, 8]]   # 2 x 3

mB = [[2, 4],[5, 7]]   # 2 x  2

matrizA = n.array(mA)
matrizB = n.array(mB)


#matrizC = matrizA.dot(matrizB)   # C = A * B

matrizC = matrizB.dot(matrizA)  # C = B * A

print(matrizC)
