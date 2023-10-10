import numpy as np

try:
    list = [input("Enter the element: ") for element in range(int(input("Enter the number of elements you have in mind: ")))]
    dict = {u_elem:0 for u_elem in np.unique(np.array(list))}

    for i in dict:
        for n in list:
            if n == i:
                dict[i] = dict[i]+1

    for u_elem in dict:
        print(f"The frequency of occurance of element {u_elem} is {dict[u_elem]}") 
        
except Exception as E:
    print(E)

else:
    print("\nProgram execution is complete")