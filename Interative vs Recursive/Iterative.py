import os

def Convert(string):
    string.rstrip()
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li

def min_iterative(list):
    min = list[0]
    index = 0
    
    if len(list > 1):
        for i in range(1, len(list)):
            if list[i]<min:
                min = list[i]
                index = i

    return min, index

n1 = int(input())
if not(n1):
    print(-1)
else:
    l1 = Convert(input())
    output = min_iterative(l1)
    print(output[1], output[0], sep = '\n')