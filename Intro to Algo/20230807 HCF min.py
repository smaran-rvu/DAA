import time

def HCF(num1, num2):
    
    t = min(num1, num2)

    while True:
        if (num1%t == 0 and num2%t == 0):
            return t
        else:    t-=1

try:
    num1, num2 = int(input("Enter num 1: ")), int(input("Enter num 2: "))
    start = time.time()
    print(f"The GCD of {num1} and {num2} is {HCF(num1, num2)}")

except Exception as e:
    print(e)

else:
    print("\nThe program execution is complete")
    print(f'\nThe time of execution of the program is {time.time() - start}')


# Solwer compared to Euclid's algorithm 
# Inputs have to be non zero