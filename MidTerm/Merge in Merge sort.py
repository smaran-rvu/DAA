def Merge(a, b):
    l = []
    i,j,k,count = 0,0,0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
        k += 1
        count+=1
    if i==len(a):
        l[k:] = b[j:]
        # for x in b[j:len(b)]:
        #     l[k] = x
    else:
        l[k:] = a[i:]

    return l,count


n1 = int(input())

if n1!=0:
    l1 = [eval(i) for i in input().split()]
    
n2 = int(input())

if n2!=0:
    l2 = [eval(i) for i in input().split()]
    
if n1==n2==0:
    print(-1)
    
elif n1==0:
    print(0)
    for i in l2: print(i, end = ' ')
    print()

elif n2==0:
    print(0)
    for i in l1: print(i, end = ' ')
    print()
    
else:
    output = Merge(l1,l2)        
    print(output[1])
    for elem in output[0]: print(elem, end = ' ')
    print()