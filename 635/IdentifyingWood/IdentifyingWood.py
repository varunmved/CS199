'''
def check(str1,str2):
    if str1-str2 == '':
        return True
    else:
        return False
'''
'''
def check(str1,str2):
    count = 0
    for i in str1:
        if i not in str2:
            count+=1
    return count == len(str2)
'''
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
