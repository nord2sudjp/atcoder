import sys
sys.setrecursionlimit(1000000)

D=[]
N=9

def dfs(n,r,pv):
    pv[n]=1
    r.append(n)
    if n==1 or all(pv):
        D.append(r)
        return
    for i in range(N):
        if pv[i]==0:
            dfs(i,r.copy(),pv.copy())
    return        
        
v=[0]*N
dfs(0,[],v)
print(D)