def canExplode(x1,y1,x2,y2,instruct):
    deltax = abs(x2-x1)
    deltay = abs(y2-y1)
    myd = {'U':0,'D':0,'L':0,'R':0}
    for instruction in instruct:
        myd[instruction] +=1
    if deltax < myd['L'] + myd['R'] and deltay < myd['D'] + myd['U']:
        return True
    else:
        return False
