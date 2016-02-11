import math 

def calcu(num):
    val = -1 +(math.sqrt(1+4.00*num))/2
    return int(round(val))

print(calcu(1))
print(calcu(2))
print(calcu(5))
print(calcu(6))
print(calcu(7))
print(calcu(1482))
