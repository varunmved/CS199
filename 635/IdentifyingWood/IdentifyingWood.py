def check(a,b):
    i = 0
    j = 0
    for i in xrange(len(a)):
        while j < len(b):
            if(a[i] == b[j]):
                j+=1
    if j == len(b):
        return 1
    else:
        return 0

print(check("abcd","abc"))
