



first=1
second=1
next=0
for x in range(3,100000):
    next=first+second
    my_string=str(next)
    if len(my_string)==1000:
        break
    first=second
    second=next
    
    
print(x)





    