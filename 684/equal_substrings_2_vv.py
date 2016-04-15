def func(s):
    myD = {}
    for i in s:
        if i not in myD:
            myD[i] =1
        else: 
            myD[i]+=1
    for a in myD.itervalues():
        print(a)
