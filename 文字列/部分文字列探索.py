#
N=int(input())
S=input()
ls=len(S)

def s(S,T):
    j=0
    for t in T:
        if t not in S[j:]:
            return(False)
        j+=S[j:].index(t)+1
    return(True)

a=0
for i in range(1000):
    T=str(i).zfill(3)
    if s(S,T):a+=1
print(a)


#
def s(S,T):
    r=False
    si=0
    for t in T:
        r1=S.find(t, si)
        if r1!=-1:
            si=r1+1
        else:
            break
    else:
        r=True
    return(r)
    



# TLE
S=input()
T=input()

a=False
ti=si=0
while ti<len(T):
    a=False
    while si<len(S):
        print(T[ti],S[si])
        if S[si]==T[ti]:
            a=True
            si+=1
            break
        si+=1
    else:
        break
    ti+=1
print(a)