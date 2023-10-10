def Convert(string):
    string.rstrip() 
    l = list(string.split(" "))
    l = [int(i) for i in l]
    return l 

m1, m2 = [], []

r1,c1 = Convert(input())
if r1>0 and c1>0:
    for i in range(r1):
        m1.append(Convert(input()))

else:
    print(0)

r2,c2 = Convert(input())
if r2>0 and c2>0:
    for i in range(r2):
        m2.append(Convert(input()))

else:
    print(0)

    
if r1==r2 and c1==c2:
    count = 0
    flag = 0
    
    for i in m1:
        if len(i) != c1:
            flag = 1
    for j in m2:
        if len(j) != c2:
            flag = 1
            
    if not flag:
        for row in range(r1):
            for col in range(c1):
                m1[row][col] += m2[row][col]
                count+=1

        for row in m1:
            for elem in row:
                print(elem, end = " ")
            print()
        print(count)
        
    else:
        print(-1)
    
else:
    print(-1)

            