# 067 - Base 8 to 9

def NtoDec(x,k):
    if x==0: return 0

    x=str(x)
    v=0
    for c in x:
        #print(c,v,v*k,v*k+int(c))
        v=v*k+int(c)
    return v


def DectoN(x,k):
    if x==0: return 0
    ans=[]
    
    while x>=1:
        ans.append(x%k)
        x=x//k
    return int(''.join(map(str,ans[::-1])))


def kton(x,k,n):
    if x==0:return 0
    x=NtoDec(x,k)
    return DectoN(x,n)



N,K=map(int,input().split())

# N=21
# K=1

for _ in range(K):
    s=str(kton(N,8,9))
    #print(s)
    s=s.replace('8','5')
    N=int(s)
print(N)
