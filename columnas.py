import random 
import numpy as np
import os
import time

while True:
    try: 
        n = int(input("Introduce el valor de columnas: "))
        if n < 10 or n > 30:
            raise ValueError("No puedes introducir un valor fuera del rango [10, 30]")
        else:
            break
    except ValueError as e:
        print(f"Error: {e}")

arreglo = np.random.randint(1, 15, n)

simbolo =  "█"

max_val = int(arreglo.max())

def graficar():
    os.system("cls")
    for i in range(max_val, 0, -1):
        for index, value in enumerate(arreglo):
            if value >= i:
                print(simbolo, end="  ")
            else:
                print(" ", end="  ")
        print()
    for i, v in enumerate(arreglo):
        if arreglo[i] >= 10:
            print(arreglo[i], end=" ")
        else:
            print(arreglo[i], end="  ")
    print()

print("Original: ")
graficar()
time.sleep(5)

for index, value in enumerate(arreglo):
    for i in range(1, n - 1):
        for j in range(0, n - i):
            if arreglo[j] > arreglo[j + 1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j + 1]
                arreglo[j + 1] = aux

                os.system("cls")
                graficar()
                time.sleep(0.25)

# NOTE: we start from the maximum since we printing from up to down (im so native english)
#       █     █
#       █     █
#       █     █
#       █  █  █               
#       █  █  █           █   
#       █  █  █           █
#       █  █  █           █
#       █  █  █  █        █  █
#       █  █  █  █        █  █
#    █  █  █  █  █        █  █
#    █  █  █  █  █        █  █
#    █  █  █  █  █        █  █
#    █  █  █  █  █  █     █  █
#    █  █  █  █  █  █  █  █  █
# █  █  █  █  █  █  █  █  █  █
# 1  6 14 12 14  8  3  2 11  8

# NOTE: each column is separated by 2 spaces, maybe TABS