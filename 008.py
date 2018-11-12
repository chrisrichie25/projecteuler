
myfile=open('no8.txt','r')
myfile=myfile.read()
numbers=myfile.split("\n")
sumstring=""
"""Two for loops are needed, one for converting the whole number into a string 
another for looping through the number and the other for looping through 
13 adjacent digits"""
listproduct=[]
product=1
listnumber=[]
maxproduct=0
for x in range(0,len(numbers)):
	sumstring+=numbers[x]
for y in range(0,len(sumstring)):
	intnumber=int(sumstring[y])
	listnumber.append(intnumber)
for a in range(0, len(listnumber)-13):
	b=1
	for i in range(0,13):
		b*=listnumber[a+i]
	if b>maxproduct:
		maxproduct=b

"""for z in range(0,len(listnumber)-12):
	for a in range(z,z+13):
		product*=listnumber[a]
	listproduct.append(product)
	product=1
	
print(listproduct)
print(max(listproduct))"""
print(maxproduct)
print(a+1)
