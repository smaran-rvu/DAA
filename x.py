import time, os

def Convert(string):
    string.rstrip()
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li

str = input()
sub = input()
n, m = len(str), len(sub)

for i in range(n-m+1):
    print(str[i:i+m])
    if str[i:i+m] == sub:
        print(i)
        break
else:
    print(-1)