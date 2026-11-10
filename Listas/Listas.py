Letras = [[[(1,2),(3,4)],
           [(5,6),(7,8)]],

          [[(9,10),(11,12)],
           [(13,14),(15,16)]]]

#Numero 13
#print(Letras[1][1][0][0])

i=0
j=0
k=0
l=0
while i<2:
    while j<2:
        while k<2:
            while l<2:
                print(Letras[i][j][k][l])
                l+=1
            k+=1
            l=0
        j+=1
        k=0
    i+=1
    j=0