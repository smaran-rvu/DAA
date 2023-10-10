import time

def Convert(string):
    li = list(string.split(" "))
    li = [int(i) for i in li]
    return li

no_of_coins = int(input())
denomination_list = Convert(input("Enter the denominations separated by spaces: ").rstrip())
denomination_list.sort()
denomination_list.reverse()

amount = int(input("Enter the money to be returned in coins: "))

print("Sorted Denominations list: ", denomination_list)


def Determine_coins_greedy(denomination_list, amount):
    coins = []
    amount_alt = amount
    if(len(denomination_list)==0): 
        print('Denominations not enough!')
        return []
    
    while True:
        for denomanation in denomination_list:
            
            if(denomanation <= amount):
                coins.append(denomanation)
                remainder = amount-denomanation
                # print(denomanation, 'chosen')
                break
        
        amount = remainder

        if not(remainder): 
            return coins
        
        if min(denomination_list)>remainder: 
            denomination_list.remove(max(denomination_list)) 
            return Determine_coins(denomination_list, amount_alt)        

def Determine_coins_brute(denomination_list, amount):
    if amount == 0:
        return 0
    
    no_coins = float('inf')
    
    for denomination in denomination_list:
        if denomination <= amount:
            temp = Determine_coins_brute(denomination_list, amount - denomination)
            no_coins = min(no_coins, temp + 1)
    
    return no_coins

coins = Determine_coins_brute(denomination_list, amount)
print(coins)#, len(coins))