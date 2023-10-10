import os

def Convert(string):
    string.rstrip()
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li


n1 = int(input())
if n1:
    l1 = Convert(input())
n2 = int(input())
if n2:
    l2 = Convert(input())

if (n1 and n2 != 0):
    l1.extend(l2)
    l1.sort()
    for i in l1: print(i, end = ' ')   

elif n1==n2==0:
    print('-1')

elif n2 == 0:
    l1.sort()
    for i in l1: print(i, end = ' ')   

elif n1 == 0:
    l2.sort()
    for i in l2: print(i, end = ' ')       