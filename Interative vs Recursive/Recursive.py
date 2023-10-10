import os

def Convert(string):
    string.rstrip()
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li

def min_recursive(list):
    
    if len(list) == 1:
        return list[0]
    
    return min(list[-1], min_recursive(list[:-1]))

n1 = int(input())
if not(n1):
    print(-1)
else:
    l1 = Convert(input())
    output = min_recursive(l1)
    print(l1.index(output), output, sep = '\n')