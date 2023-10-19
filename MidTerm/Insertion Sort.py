n = int(input())

if n>0:

    l = input().split()
    l = [eval(i) for i in l]
    c1, c2 = 0 , 0
    
    for i in range(1, len(l)):

            temp = l[i]
            j = i-1
            while j >= 0 :
                c1+=1
                if temp < l[j]:
                    l[j + 1] = l[j]
                    c2 += 1
                    j -= 1
                else:
                    break
            l[j + 1] = temp
    
    print(c1)
    print(c2)
    for elem in l:
        print(elem, end = ' ')

else:
    print(-1)  