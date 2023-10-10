def Convert(string):
    string.rstrip() 
    l = list(string.split(" "))
    l = [int(i) for i in l]
    return l 


n = int(input())
# print(n)

if n>0:
    l = Convert(input())
    # print(l)
    
    #     # METHOD 1 - Worse time and Space Effeciency
#    d = {}

#     # Finding frequency of each element occuring in l
#     for i in l:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
    
#     # print(d)
#     # Finding if more than one occurance has been observed for every element
#     flag = 1
#     for j in d:
#         if d[j]>1:
#             flag = -1
#             break

#     print(flag)
    
    # METHOD 2 - Better time and space effeciency
    flag = 0
    for i in l:
        l.remove(i)
        if i in l:
            flag = 1
            print(-1)
            break
    if flag==0:
        print(1)
        
else:
    print(0)
