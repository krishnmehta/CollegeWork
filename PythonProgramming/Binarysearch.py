#19 Krishn Mehta
arr = [2,3,4,5,6,7,8,9,10]
key = 9
def binarySearch2(arr,x) :
    l = 0
    r = len(arr) - 1
    while l <= r :
        mid = int((l+r)/2)
        if arr[mid] == key :
            return mid
        elif arr[mid] > x :
            r = mid + 1
        else :
            l = mid + 1
    return -1
print('Element found at index : ',binarySearch2(arr,key))
