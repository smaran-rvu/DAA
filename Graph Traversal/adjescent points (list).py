n = int(input())

class Node:
    
    def __init__(self, data):
        self.next = None
        self.data = data

class Tree:
    
    def __init__(self, data):
        self.head = Node(data)

    def insert_front(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    def insert_rear(self, data):
        itr = self.head
        if not(itr):
            self.insert_front(data)
            return
        
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)
    
    def delete_front(self):
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def print_list(self):
        itr = self.head
        str_temp = ''
        while itr:
            str_temp += str(itr.data)+','
            itr = itr.next
        print(str_temp[:len(str_temp)-1])
        
    def print_len(self):
        itr = self.head
        len = 0
        while itr:
            len += 1
            itr = itr.next
        return len

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
        vertexList = [Tree(i) for i in range(n)]
        for edge in l:
            vertexList[edge[0]-1].insert_rear(edge[1])

        for vertex in vertexList:
            vertex.delete_front()
            # vertex.print_list()
            # print()
        
        print(vertexList[v-1].print_len())
        vertexList[v-1].print_list()

        
else:
    print(-1)