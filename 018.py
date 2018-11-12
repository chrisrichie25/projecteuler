"""myfile=open('no18.txt','r')
myfile=myfile.read()
numbers=myfile.split("\n")
print(numbers)
for x in range(0,len(numbers)):
	numbers[x].split()
print(numbers)
"""
with open("no18.txt") as no18:
    lines = [line.split() for line in no18]
number1=0
number2=0
for x in range(0,((len(lines))-1)):
	count=0
	for y in range(0,len(lines[x])-1):
		number1=int(lines[x][y])+int(lines[x+1][count])
		print(number1)
		number2=int(lines[x][y])+int(lines[x+1][count+1])
		lines[x+1][count]=number1
		lines[x+1][count+1]=number2
		count+=2
	
print(max(lines[14]))

