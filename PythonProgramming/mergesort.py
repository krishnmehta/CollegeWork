#19 Krishn Mehta
def mergesort(listA):
    if(len(listA)>1):
        mid=int(len(listA)/2)
        lefthalf=listA[:mid]
        righthalf=listA[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i=j=k=0
        while i<len(lefthalf) and j<len(righthalf):
            if(lefthalf[i]<righthalf[j]):
                listA[k]=lefthalf[i]
                i=i+1
            else:
                listA[k]=righthalf[j]
                j=j+1
            k=k+1
        while i<len(lefthalf):
            listA[k]=lefthalf[i]
            i=i+1
            k=k+1                

        while j<len(righthalf):
            listA[k]=righthalf[j]
            j=j+1
            k=k+1

listA=[4,3,1,4,7,6,8]
mergesort(listA)
print(listA)