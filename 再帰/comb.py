def comb(n,l):
    if n==0:
        ans.append(l)
        return
    
    comb(n-1,l+["t"])
    comb(n-1,l+["f"])
ans=[]
comb(3,[])
print(ans)