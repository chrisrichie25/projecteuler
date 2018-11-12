list=[1,2]
sum=0
for x in range(0,200):
    sum=list[x]+list[x+1]
    list.append(sum)
    if list[len(list)-1]>=4000000:
        list.remove(list[len(list)-1])
        break
       
    
print("{0}".format(list[len(list)-1]))

list2=[]
for x in range(0,len(list)):
    if list[x]%2==0:
        list2.append(list[x])
sum2=0
for y in range(0,len(list2)):
    sum2+=list2[y]

print("The sum is {0}".format(sum2))




    

    

 
    
    

    