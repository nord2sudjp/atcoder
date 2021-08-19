# 063 - Monochromatic Subgrid

H,W=map(int,input().split())
P=[list(map(int,input().split())) for _ in range(H)]

def f(S):
    l_S=len(S)
    d={}
    s=S[0]
    l_s=len(s)
    for i in range(l_s):
        t=s[i]
        for j in S[1:]:
            if t!=j[i]:
                t=-1
                break
        if t!=-1:
            x=d.get(t,0)
            d[t]=x+l_S
    return d

ans={}
for i in range(2**H): 
    t=[]
    for j in range(H): 
        if (i>>j&1):
            t.append(P[j])
    # Verify same value.
    d=f(t)
    for k,v in d.items():
        ans_v=ans.get(k,0)
        if ans_v<v:
            ans[k]=v

print(max(ans.values()))    