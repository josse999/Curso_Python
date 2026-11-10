ListaCompra = []
Option = ""
Active = True
i=1

print("{}".format("*"*len("Lista de compra")))
print("Lista de compra")
print("{}".format("*"*len("Lista de compra")))

#Llenar lista de compra
while Active:
    Option = input("\nIngrese el producto que desea agregar, [Q] para terminar:\n")
    if Option not in {"Q","q"}:
        if Option not in ListaCompra:
            ListaCompra.append(Option)
        else:
            print("\nEse producto ya esta en la lista")
    else:
        Active = False

#Imprimir lista de compra
for Item in ListaCompra:
    print("{}. {}".format(i,Item))
    i += 1
