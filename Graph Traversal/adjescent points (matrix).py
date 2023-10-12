n = int(input())

if n>0:
    l = []
    while(1):
        x = input().rstrip()
        temp = x.split()
        temp = [eval(x) for x in temp]
        # print(x, temp)
        
        if len(temp) > 1:
            l.append(temp)
        else:
            v = temp[0]
            break
            # print("Vertex:", v)
         
    if n == 1:
        print(v)
    
    else:
        matrix = [[0 for i in range(n)] for j in range(n)]
        for edge in l:
            matrix[edge[0]-1][edge[1]-1] = 1
        adj = []
        for i in range(len(matrix[v-1])):
            if matrix[v-1][i] == 1:
                adj.append(i+1)
        
        print(len(adj))
        str_ = ''
        for vertex in adj:
            str_ += (str(vertex)+',')
        print(str_[0:len(str_)-1])
                
        
else:
    print(-1)