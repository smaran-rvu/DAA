def Euclid(num1, num2):
    if num2==0:
        return num1
    
    num1, num2 = num2, num1 % num2
    return Euclid(num1,num2)

num1, num2 = [eval(i) for i in input().split(' ')]
print(Euclid(max(num1, num2), min(num1,num2)))
