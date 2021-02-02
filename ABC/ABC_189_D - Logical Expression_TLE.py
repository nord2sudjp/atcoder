N=int(input())
S=[input() for _ in range(N)]
S=S[::-1]


A=[1]

def comb(n,l):
    if n==N:
        ans.append(l)
        return
    s=S[n]
    a=l[-1]
    n+=1
    if s=="AND":
        if a==1:
            comb(n,l+[1,1])
        else:
            # 01, 10, 00
            comb(n,l+[0,1])
            comb(n,l+[1,0])
            comb(n,l+[0,0])
    else: # or
        if a==1:
            # 01, 10, 11
            comb(n,l+[0,1])
            comb(n,l+[1,0])
            comb(n,l+[1,1])
        else:
            # 00
            comb(n,l+[0,0])
ans=[]
comb(0,A)
print(len(ans))
