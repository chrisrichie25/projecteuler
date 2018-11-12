
#The following code is designed to find the 10001'st prime number
prime=[2,3,5,7,11,13,17,19]
count=23
while len(prime)<10001:
    is_prime = True
    for x in range(0,len(prime)):
        if count%prime[x]==0:
            is_prime = False
            break
    if is_prime:
        prime.append(count)
    count+=2
    
print("The 10001st prime number is {0}".format(prime[11]))
