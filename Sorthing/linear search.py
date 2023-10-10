import time
def Convert(string):
    li = list(string.split(" "))
    return li


try:
    l = Convert(input("Enter the elements of the list separated by spaces:"))
    k = input("enter the key: ")

except Exception as e:
    print(e)

else:
    start = time.time()
    if(len(l) != 0):
        for i in range(len(l)):
            if k==l[i]:
                print("Element found!")
                break
        else:
            print("Element not found")
    else:
        print("Empty list")
    print(f"Exec time: {(time.time() - start)*1000} ms")
