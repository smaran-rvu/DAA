import time, os

def Convert(string):
    string.rstrip()
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li

def bubble_sort(arr):
    n = len(arr)
    c1,c2 = 0,0
    for i in range(n):
        for j in range(0, n - i - 1):
            c1+=1
            if arr[j] > arr[j + 1]:
                c2+=1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return c1,c2
        
no_of_elements = int(input())

if no_of_elements == 0:
    print("-1\n-1\n-1")

else:
    d_list = Convert(input(""))

    tops = no_of_elements -1
    flag = 0
    count_comp, count_swap = 0,0

    i = 0

    if len(d_list)==1:
        print(f'0\n0\n{d_list[i]}')

    else:
        count_comp, count_swap = bubble_sort(d_list)
        print(count_comp)
        print(count_swap)
        # print()
        for i in d_list: print(i, end = ' ')


