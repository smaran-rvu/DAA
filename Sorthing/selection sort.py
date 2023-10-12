def Convert(str):
    l = str.split(' ')
    return l

def Selectionsort(l, n):
    
    count_comp, count_swap = 0,0
    for i in range(n-1): # n-2 but the last element is ommitted that's why n-1 
        min = i
        
        for j in range(i+1,n): # n-1 but the last element is ommitted that's why n
            count_comp += 1
            if l[min]>l[j]:
                min = j
        
        # print(i,min)
        if l[i]!=l[min]:
            count_swap += 1
            temp = l[min]
            l[min] = l[i]
            l[i] = temp    
            
    print(count_swap)
    print(count_comp)
    return l

n = int(input())
if n == 0:
    print(-1)

else:
    l = Convert(input())
    if n==1:
        print(l[0])
    else:
        Selectionsort(l, n)
        for elem in l: print(elem, end = ' ')
