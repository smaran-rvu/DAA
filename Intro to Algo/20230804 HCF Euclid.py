import time

# Euclid's algorithm

'''
Note: 2 input integers m,n SHOULD BE NON NEGATIVE

If n = 0, return m and stop
Otherwise
    Divide m by n and assign a value of the remainder to r
    Assign the val of n to m and the val of r to n.
    Recurse to zero check
'''

def Euclid(num1, num2):
    if num2==0:
        print(f"returning num1 {num1}")
        return num1
    
    print(f"num1 = {num1} , num2 = {num2}")
    num1, num2 = num2, num1 % num2
    return Euclid(num1,num2)

try:
    num1, num2 = int(input("Enter num 1: ")), int(input("Enter num 2: "))
    start = time.time()
    print(f"The GCD of {num1} and {num2} is {Euclid(max(num1, num2), min(num1,num2))}")

except Exception as e:
    print(e)

else:
    print("\nThe program execution is complete")
    print(f'\nThe time of execution of the program is {time.time() - start}')
