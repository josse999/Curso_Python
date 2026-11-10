frutas = ["Manzanas","Peras","Guayaba","Mango"]
vocales = ["a","e","i","o","u"]
num_vocales = 0
i=0
for item in frutas:
    for cosa in item:
        if cosa in vocales:
            num_vocales += 1

print(num_vocales)

