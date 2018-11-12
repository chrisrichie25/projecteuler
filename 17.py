# A program to find the sum of the letters of numbers from 1 to 990


one=(len("one"))*90
two=len("two")
three=len("three")
four=len("four")
five=len("five")
six=len("six")
seven=len("seven")
eight=len("eight")
nine=len("nine")
ten=len("ten")
eleven=len("eleven")
twelve=len("twelve")
thirteen=len("thirteen")
fourteen=len("fourteen")
fifteen=len("fifteen")
sixteen=len("sixteen")
seventeen=len("seventeen")
eighteen=len("eighteen")
nineteen=len("nineteen")
twenty=len("twenty")
thirty=len("thirty")
forty=len("forty")
fifty=len("fifty")
sixty=len("sixty")
seventy=len("seventy")
eighty=len("eighty")
ninety=len("ninety")
hundred=len("hundredand")
hundredfirst=(len("hundred")*9)+(one+two+three+four+five+six+seven+eight+nine)
thousand=len("onethousand")
sumteen=ten+eleven+twelve+thirteen+fourteen+fifteen+sixteen+seventeen+eighteen+nineteen
sumbig=(twenty*10)+(thirty*10)+(forty*10)+(fifty*10)+(sixty*10)+(seventy*10)+(eighty*10)+(ninety*10)
sumhundred=((one+hundred)*99)+((two+hundred)*99)+((three+hundred)*99)+((four+hundred)*99)+((five+hundred)*99)+((six+hundred)*99)+((seven+hundred)*99)+((eight+hundred)*99)+((nine+hundred)*99)



#Sum of the numbers from one to a thousand
sumtwo=(two*9)*10
sumthree=(three*9)*10
sumfour=(four*9)*10
sumfive=(five*9)*10
sumsix=(six*9)*10
sumseven=(seven*9)*10
sumeight=(eight*9)*10
sumnine=(nine*9)*10
sumteentotal=sumteen*10
sumbigtotal=sumbig*10
sumhundredandthousand=sumhundred+hundredfirst+thousand

#Total sum from 1 to a thousand
total=sumone+sumtwo+sumthree+sumfour+sumfive+sumsix+sumseven+sumeight+sumnine+sumteentotal+sumbigtotal+\
		sumhundredandthousand
print(total)

