#19 Krishn Mehta
#Karatsuba Algorithm
X = int(input("Enter Number 1 "))
Y = int(input("Enter Number 2 "))

def karatsuba(X,Y):
    #base case
    if X<10 or Y<10:
        return X*Y
    m = max(len(str(X)),len(str(Y)))

    if m%2!=0:
        m-=1
    a,b = divmod(X, 10**int(m/2))
    c,d = divmod(Y, 10**int(m/2))

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a+b), (c+d)) - ac -bd

    return ((ac*(10**m)) + ((ad_bc)*(10**int(m/2)))+bd) # karatsuba equation


s = karatsuba(X, Y)
print(s)