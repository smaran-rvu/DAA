def Pivot(l, p, r, pi):
    pivot = l[pi]
    swaps = 0
    i = p-1
    
    for j in range(p, r):
        if l[j] <= pivot:
            i += 1
            if l[j] != l[i]:
                swaps += 1
            # print("swapping", l[j],"<->",l[i])
            l[i], l[j] = l[j], l[i]
            
    l[pi], l[i+1] = l[i+1], l[pi]
    return i+1, swaps+1

n = int(input())

if n==0:
    print(-1)

else:
    l = [eval(i) for i in input().split()]
    pi = int(input())
    if n==1:
        print(l[0])
    
    else:
        output = Pivot(l,0,n-1,pi)        
        print(output[1])
        for elem in l: print(elem, end = ' ')
        print()
        print(output[0])