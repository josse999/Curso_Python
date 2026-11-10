import string
print("Espacios, Puntos, Comas y Mayusculas de un texto\n")

text = input("Ingrese la frase que quiere comparar\n")

space = 0
dot = 0
coma = 0
cap = 0
#for de espacios, puntos y comas
for item in text:
    if item == " ":
        space += 1
    if item == ".":
            dot += 1
    if item == ",":
        coma += 1
    if item.isupper():
        cap += 1

print("Espacios = {}\nPuntos = {}\nComas = {}\nMayusculas = {}".format(space,dot,coma,cap))


