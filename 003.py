from math import sqrt
list=[] 
root=int(sqrt(600851475143))

for x in range(3,root,2):
    if 600851475143%x==0:
        list.append(x)
        list.append(int(600851475143/x))

prime=[71]
for y in range(0,13):
    ret=int(sqrt(list[y]))
    is_prime=True
    for r in range(71,list[y],2):
        if list[y]%r==0:
            is_prime=False
            break
    if is_prime:
        prime.append(list[y])
            
print(max(prime))
    