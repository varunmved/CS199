#Varun Ved
#IdentifyingWood

#return wood if s2 in s2

def check(s1,s2):
    s1d = {}
    s2d = {}
    for i in s1:
        if i not in s1d:
            s1d[i] = 1
        else:
            s1d[i]+=1
    for j in s2:
        if j not in s2d:
            s2d[j] = 1
        else:
            s2d[j]+=1

    for keys in s1d.iteritems():
        print(keys)
    
    print('aaa')
    for keys2 in s2d.iteritems():
        print(keys2)

check("asdefgh","asdf")
