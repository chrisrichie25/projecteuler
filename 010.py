from math import sqrt
#The following code is designed to find the 10001'st prime number
count=23
total=77
while count<2000000:
    is_prime = True
    root=int(sqrt(count))
    for x in range(3,root+1,2):
        if count%x==0:
            is_prime = False
            break
    if is_prime:
        total+=count
    count+=2
    
print("The 10001st prime number is {0}".format(total))
