lista=[]
listb=[]
listc=[]
for c in range(500,1,-1):
    for b in range(1,400):
        for a in range(300,1,-1):
            sumall=a+b+c
            if sumall==1000:
                lista.append(a)
                listb.append(b)
                listc.append(c)
lista1=[]
listb1=[]
listc1=[]
for x in range(0,len(lista)):
    if lista[x]<listb[x] and listb[x]<listc[x]:
        lista1.append(lista[x])
        listb1.append(listb[x])
        listc1.append(listc[x])
for y in range(0,len(lista1)):
    if lista1[y]**2+listb1[y]**2==listc1[y]**2:
        print(lista1[y])
        print(listb1[y])
        print(listc1[y])
        break
print(lista1[y]*listb1[y]*listc1[y])

    
    
    

    