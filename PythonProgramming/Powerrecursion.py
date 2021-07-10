#19 Krishn Mehta
#Find the power using recursion
'''def power(x,n):
    if(n==0):
        return 1
    elif(int(n%2)==0):
        return (power(x, int(n/2))*power(x,int(n/2)))
    else:
        return(x*power(x,int(n/2))*power(x,int(n/2)))'''

#Most Optimized way
def power(x,n):
    if(n==0):
        return 1
    flag=power(x, int(n/2))
    if(int(n%2)==0):
        return (flag*flag)
    else:
        return(x*flag*flag)
a = int(input())
b = int(input())
print(power(a, b))