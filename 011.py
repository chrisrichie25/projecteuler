myfile=open('no11.txt','r')
myfile=myfile.read()
mainarray=myfile.split("\n")
sumstring=""
coloumarray=[]

for x in range(0,len(mainarray)):
	rowarray=mainarray[x].split(" ")
	coloumarray.append(rowarray)
print(coloumarray)

for x in range(0,len(coloumarray)):
	for y in range(0,len(coloumarray[x])):
		coloumarray[x][y] = int(coloumarray[x][y])
print(coloumarray)

def multiplyindir(a,d):
		if d = 1