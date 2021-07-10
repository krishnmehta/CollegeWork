#19 Krishn Mehta
def countsort(arr):
    freq = [0 for i in range(256)]
    for j in arr:
        freq[ord(j)]+=1 #incrementing the count for the character
    sorted_string = ""
    for i in range(256):
        for j in range(freq[i]):
            sorted_string+=chr(i)
    return sorted_string
'''
arr = "problemsolvingusingpython"
sorted_string = countsort(arr)
print(sorted_string)
'''


n = int(input())
arr=[]
for i in range(0,n):
    j = int(input())
    arr.append(j)
print(arr)        
#arr = [7,2,1,6,8,5,3,4]
#n = len(arr)
arr1 = countsort(arr)
for i in range(0,n):
    print(arr1[i])
    
    
n = int(input())

ar = []
for i in range(n):
    if i < n//2:
        numX, striX = input().strip().split()
        ar.append((int(numX),'-'))
    else:
        numX,striX = input().strip().split()
        ar.append((int(numX),striX))

ar.sort(key=lambda tup: tup[0]) 
print(*[x[1] for x in ar])