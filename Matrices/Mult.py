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
    
if c1==r2:
    
    flag = 0
    
    if len(m1)!=r1 or len(m2)!=r2:
        flag = 1
    
    for i in m1:
        if len(i) != c1:
            flag = 1
    for j in m2:
        if len(j) != c2:
            flag = 1
    
    if not flag:
        m3 = [[0 for y in range(c2)] for x in range(r1)]
        mult, add = 0, 0

        for a in range(r1):
            for b in range(c2):
                sum = 0
                for i in range(c1):
                    # m3[a][b] += m1[a][i]*m2[i][b]
                    sum += m1[a][i]*m2[i][b]
                    mult += 1
                add+=1
                m3[a][b] = sum

        for row in m3:
            for elem in row:
                print(elem, end = " ")
            print()
        print(mult,mult-add)
    
    else:
        print(-1)

else:
    print(-1)