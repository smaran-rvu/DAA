import time

def Convert(string):
    li = list(string.split(" "))
    if (type(li[1]) == 'int'): li = [int(i) for i in li]
    return li

def BS(list, key):
    j= len(list)-1
    i = 0
    
    tea = (j-i)//2

    while (i<=j):
        
        print(f"i = {i}, j = {j}, tea = {tea}")
        
        if key==list[tea] or key==list[j]:
            print("Element found!")
            return
        
        elif (key < list[tea]):
            j = tea-1
            tea = (j-i)//2

        elif (key > list[tea]):
            i = tea+1
            tea = tea + (j-i)//2
            

    else:
        
        print("Element not found")

try:
    l = Convert(input("Enter the elements of the list separated by spaces :"))
    k = input("enter the key: ")

except Exception as e:
    print(e)

else:
    start = time.time()
    if(len(l) != 0):
        l.sort()
        print(l)
        BS(l,k)
    else:
        print('Empty list')
    print(f"Exec time: {(time.time() - start)*1000} ms")
