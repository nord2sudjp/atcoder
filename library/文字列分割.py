# 
from itertools import groupby
s='aabbccdeeeff'

ans=groupby(s)

l=[''.join(g) for k, g in groupby(s)] 
print(l)


# これは使わない
def divstr(S):
    S=''.join([S,'$'])

    ans=[]
    L=len(S)

    lake=S[0]
    i=1
    while i<L:
        if S[i]=='$':
         ans.append(lake)
        elif lake[0] != S[i]:
         ans.append(lake)
         lake=S[i]
        else:
         lake+=S[i]
        i+=1
    return ans
