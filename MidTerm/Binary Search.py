comp = 0

def binarySearch(arr, key, l, r):
    global comp
    
    mid = (l+r)//2
    # print(arr[l:r+1])
    # print(l,r, mid)
    
    if l>r:
        return -1
    
    comp += 1
    if key == arr[mid]:
        return mid
    
    elif key < arr[mid]:
        # print("lside")
        r = mid - 1
        return binarySearch(arr, key, l, r)

    elif key > arr[mid]:
        # print("rside")
        l = mid + 1
        return binarySearch(arr, key, l, r)
    
n = int(input())

if  n > 0:
    arr = [eval(i) for i in input().split(' ')]
    key = int(input())
    index = binarySearch(arr, key, 0, len(arr)-1)
    
    print(comp)
    print(index)
else:
    print(-1)