def b(a,k):
    a = sorted(a)
    return sum(a[:k])

t0 =b([1, 1, 1, 1, 1], 5)
t1 =b([39, 47, 36, 50, 36, 25, 16, 5, 20, 27, 19, 41, 2, 25, 21, 20, 16], 8)

print(t0,t1)
