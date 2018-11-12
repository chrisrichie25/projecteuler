numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
multiple=[2,5,2,0]
count=2520
while len(multiple)<5:
    is_true=True
    for x in range(0,len(numbers)):
        if count%numbers[x]!=0:
            is_true=False
            break
    if is_true:
        multiple.append(count)
    count+=20
    
print(multiple)