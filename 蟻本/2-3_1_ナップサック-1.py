f=lambda:map(int,input().split())
#N,W=f()
#*S,=f()
#*V,=f()

N=4
W=5
S=[2,1,3,2]
V=[3,2,4,2]

def rec(i,j): 
    # i=使用した荷物(初期値=0,条件i<N)
    # j=利用できる重量(初期値=W, 条件0<=j)
    r=0
    if (i==N): # 荷物はない
        r=0
    elif j<S[i]: # この荷物は入らない
        r=rec(i+1,j)
    else:
        r=max(rec(i+1,j), rec(i+1,j-S[i])+V[i])
    return(r)
print(rec(0,W))