n = int(input())

def Merge(l, a, b):

    i,j,k = 0,0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            l[k] = a[i]
            i += 1
        else:
            l[k] = b[j]
            j += 1
        k += 1

    if i==len(a):
        l[k:] = b[j:]
        # for x in b[j:len(b)]:
        #     l[k] = x
    else:
        l[k:] = a[i:]

def Merge_Sort(l):

    if len(l)>1:
        a = (l[:len(l)//2])
        b = (l[len(l)//2:])
        Merge_Sort(a)
        Merge_Sort(b)
        Merge(l,a,b)

if n==0:
    print(-1)

else:
    str = input().rstrip()
    l = str.split(' ')
    l = [eval(i) for i in l]

    if n==1:
        print(l[0])
    
    else:
        Merge_Sort(l)
        for i in l: print(i, end = ' ')