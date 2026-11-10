import random
import os

vidaIPikachu = 80
vidaPikachu = vidaIPikachu
vidaISqrt = 90
vidaSqrt = vidaISqrt

print("Bienvenido al combate Pokemon!")

while vidaPikachu >0 and vidaSqrt >0:
    CpuOption = random.randint(1, 2)

    #Barra de vida
    barraSqrt = int((10*vidaSqrt)/vidaISqrt)
    barraPikachu = int((10 * vidaPikachu)/vidaIPikachu)
    print("squirtle: [{}{}] ".format("~"*barraSqrt," "*(10-barraSqrt)))
    print("pikachu:  [{}{}] ".format("~"*barraPikachu," "*(10-barraPikachu)))

    #Turno de pikachu
    print("\n\n\nTurno de pikachu!")
    if CpuOption == 1:
        vidaSqrt -= 10
        print("Pikachu utilizo el ataque de Bda voltio, squirtle pierde 10 puntos de vida")
    elif CpuOption == 2:
        vidaSqrt -= 11
        print("Pikachu utilizo el ataque de Onda trueno, squirtle pierde 11 puntos de vida")
    input("\nEnter para continuar...")
    # No funciona en la terminal de pycharm
    os.system("cls")

    #Barra de vida
    barraSqrt = int((10 * vidaSqrt) / vidaISqrt)
    barraPikachu = int((10 * vidaPikachu) / vidaIPikachu)
    print("squirtle: [{}{}] ".format("~" * barraSqrt, " " * (10 - barraSqrt)))
    print("pikachu:  [{}{}] ".format("~" * barraPikachu, " " * (10 - barraPikachu)))

    #Turno de squirtle
    print("\n\n\nTurno de squirtle!")
    option = input("\nIngresa el ataque que quieres realizar\n\n[A].Placaje\n[B].Pistola Agua\n[C].Burbuja\n").upper().strip()
    while option not in ["A","B","C",""]:
        print("La opcion ingresada no es correcta")
        option = input("\nIngresa el ataque que quieres realizar\n\n[A].Placaje\n[A].Pistola Agua\n[A].Burbuja\n").upper().strip()
    if option == "A" :
        vidaPikachu -= 10
        print("utilizaste el ataque de placaje, pikachu pierde 10 puntos de vida!")
    elif option == "B":
        vidaPikachu -= 12
        print("utilizaste el ataque de pistola agua, pikachu pierde 12 puntos de vida!")
    elif option == "C":
        vidaPikachu -= 9
        print("utilizaste el ataque de burbuja, pikachu pierde 9 puntos de vida!")
    else:
        print('"No hiciste nada"')
    input("\nEnter para continuar...")
    #No funciona en la terminal de pycharm
    os.system("cls")

#Final
if vidaSqrt > vidaPikachu:
    print("Felicidades, Ganaste!!")
else:
    print("Pikachu gana, suerte para la proxima")
