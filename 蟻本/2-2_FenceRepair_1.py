#N=3
#L=[8,5,8]

N=int(input())
*L,*=map(int,input().split())
a=0

def rep(L):
    if len(L)==1:return(0)
    t=L[0]+L[1]
    L=L[2:]
    L.append(t)
    return t+rep(L)

print(rep(L))