def valueOfString(s,k):
    myD =  {}
    for i in s:
        if i not in myD:
            myD[i] = 1
        else:
            myD[i] +=1
    sumR = 0
    for a in myD.itervalues():
        this = pow(int(a),2)
        sumR +=this
    return sumR

cases = ['ada',"abacaba","abacaba","abacaba", "abc"]
for case in cases:
    print(valueOfString(case,1))
