

    

    

power_summation=[]
summation=0
for x in range(0,100):
    for y in range(0,100):
        power=x**y
        my_string=str(power)
        for z in range(0,len(my_string)):
            summation+=int(my_string[z])
            power_summation.append(summation)
print(power_summation[100])




    