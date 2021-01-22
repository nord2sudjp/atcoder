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