sumpowers=0
for x in range(1,1001):
    powers=x**x
    sumpowers+=powers
    
my_string=str(sumpowers)
print(my_string[len(my_string)-10:len(my_string)])
