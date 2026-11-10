import numbers
Lista = []
Option = None
Active = True
i = 1

#Llenar la lista
while Active:
    Option = input("Ingrese el numero {} de la lista, '[S] para parar'\n".format(i))
    if Option not in {"S","s"}:
        Lista.append(int(Option))
        i += 1
    else:
        Active = False

Higher = Lista[0]
Lower = Higher
#Comparacion
for Item_1 in Lista[1:]:
        if Item_1 > Higher:
            Higher = Item_1
        if Item_1 < Lower:
            Lower = Item_1

print("Mayor: {}\nMenor: {}".format(Higher,Lower))

