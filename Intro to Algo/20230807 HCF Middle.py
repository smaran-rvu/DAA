import time
import numpy as np

def prime_factors(n):

    pf = []
    spf = [0 for i in range(n+1)]
    spf[1] = 1
    for i in range(2, n+1):
        spf[i] = i
    for i in range(4, n+1, 2):
        spf[i] = 2
  
    for i in range(3, int(n**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i
                      
    while n != 1:
        pf.append(spf[n])
        n = n // spf[n]

    return pf

def common_factors(l1, l2):
    common = []
    for i in l1:
        for j in l2:
            if i==j:
                common.append(i) #np.intersect1d(l1, l2, assume_unique= True, return_indices= False)
                l2.remove(j)
    return common

def middle(num1, num2):
    
    l1 = prime_factors(num1)
    l2 = prime_factors(num2)

    print(l1)
    print(l2)

    common = common_factors(l1, l2)
    
    HCF = 1
    print(common)
    for factor in common:
        HCF*=factor
    
    return HCF

try:
    num1, num2 = int(input("Enter num 1: ")), int(input("Enter num 2: "))
    start = time.time()
    print(f"The GCD of {num1} and {num2} is {middle(max(num1, num2), min(num1,num2))}")

except Exception as e:
    print(e)

else:
    print("\nThe program execution is complete")
    print(f'\nThe time of execution of the program is {time.time() - start}')
