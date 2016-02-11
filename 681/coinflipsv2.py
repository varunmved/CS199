def flip(coins):
    count = 0
    if len(coins) < 3:
        if len(set(coins))== len(coins):
            count = 2
        else:
            count = 0
    else:
        for i in range(1,len(coins)-1):
            if coins[i-1] != coins or coins[i] != coins[i+1] and coins[i] != '':
                print('\n')
                print(coins[i-1])
                print(coins[i])
                print(coins[i+1])

                count+=1
    return count

a = ['H','T']
b = ['H','H','T''H','H','H']
c = ['H','H''H','T','T','T','H','H','H','T','T','T','H','T','H','T','H']
d = ['H','H','H']


#print(flip(a))
print(flip(b))
#print(flip(c))
#print(flip(d))

