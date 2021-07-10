#19 Krishn Mehta
text = "python"
pattern = "th"

x = len(text)
y = len(pattern)
d = 256 # pitional base (radix base)
flag = 0


# find the sum for the pattern
sumP = 0
for i in range(y) :
    sumP = sumP + (ord(pattern[i])*(d**(y-i-1)))
#print(sumP)


# sum for text
sumT = 0
for i in range(y) :
    sumT = sumT + (ord(text[i])*(d**(y-i-1)))

if sumP == sumT :
    print('Pattern is present in the text')

# rolling hash functn
for i in range(y,x) :
    sumT = (sumT - (ord(text[i-y]))*(d**(y-1)))*d + ord(text[i])

    if sumP == sumT :
        flag = 1
        print("Pattern is present at ",i-y+1)
if flag == 0 :
    print("Pattern is not present")



# not done modulus approach
# here we need to make sure that if modulo matches then we need to check char by char for
# string and pattern because mdulo may have same ans for differnet pattern
