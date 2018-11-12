factorial=1
for x in range(100,0,-1):
    factorial*=x
    
my_string=str(factorial)
total=0
for x in range(0,len(my_string)):
    integer=int(my_string[x])
    total+=integer
    
print(total)