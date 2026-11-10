import math
print("Tabla de multiplicar personalizada")
num_1 = input("\nIngrese el numero que quiere en la tabla\n")
num_2 = 1

while num_2 <=10:
    num_3 = int(num_2)*int(num_1)
    if num_3%2 == 0:
        print("{} x {} = {}".format(num_1,num_2,num_3))
    num_2 += 1