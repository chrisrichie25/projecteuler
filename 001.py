total=0
for x in range(5,1000,5):
    total=total+x
    
print("{0}".format(total))
total1=0
for x in range(3,1000,3):
    total1=total1+x
print("{0}".format(total1))
total2=0
for x in range(15,1000,15):
    total2=total2+x
finaltotal=total+total1-total2
print("Therefore the sum of the multiples is {0}".format(finaltotal))


