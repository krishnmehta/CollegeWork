#19 Krishn Mehta
def partition(arr,low,high):
    pivot = arr[high]
    pIndex=low
    for j in range(low,high):
        if(arr[j]<pivot):
            arr[j],arr[pIndex] = arr[pIndex],arr[j] #Swapping
            pIndex = pIndex + 1

    arr[pIndex],arr[high]=arr[high],arr[pIndex]
    return pIndex

def quicksort(arr,low,high):
  if(low<high):
      pIndex = partition(arr,low,high) #Index of pivot element
      quicksort(arr,low,pIndex-1) #left of pivot element
      quicksort(arr,pIndex+1,high) #right of pivot element

arr = [7,2,1,6,8,5,3,4]
n = len(arr)
quicksort(arr,0,n-1)
print(arr)