from math import sqrt
"""triangle=[]
trianglenext=0
divcount=1
while divcount <=501:
    trianglenext+=divcount
    
    for x in range(1,int(trianglenext/2)-1):
        count=0
        if trianglenext%x==0:
            count+=2
        if count>500:
            print(trianglenext)
            break
            
    divcount+=1
    triangle"""

"""def divider(number):
	count=0
	if number%2==0:
		for z in range(1,number+1,1):
			if number%z==0:
				count+=1
	elif number%2!=0:
		for z in range(1,number+1,2):
			if number%z==0:
				count+=1
	return(count)"""

trinumber=0
#finding the triangle numbers first
trilist=[]
count1=0
count=0
trinumber=0

while count<=500:
	count=0
	count1+=1
	trinumber+=count1
	sqrttri=int(sqrt(trinumber))
	for z in range(1,sqrttri+1):
		if trinumber%z==0:
			count+=2
	
print(count)
print(trinumber)
print(count1)
