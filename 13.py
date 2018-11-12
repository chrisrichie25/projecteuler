#A program to calculate the first ten digits of the sum of one hundred 50-digit number
myfile=open('no13.txt','r')
myfile=myfile.read()
numbers=myfile.split("\n")
sumnumbers=0
for x in range(0,len(numbers)):
	integer=int(numbers[x])
	sumnumbers+=integer

numberstring=str(sumnumbers)
print(numberstring[0:10])