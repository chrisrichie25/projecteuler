

palindrome=[]
for x in range(999,99,-1):
    for y in range(999,99,-1):
        multiplication=x*y
        myn=str(multiplication)
        rev=myn[len(myn):0:-1]
        rev2=rev+myn[0]
        reverse=int(rev2)
        if reverse==multiplication and reverse>900000:
            palindrome.append(multiplication)
print(palindrome[0])



