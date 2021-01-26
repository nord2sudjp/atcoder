import copy
#N=2
#RC=[[2,2],[5,3]]

N=int(input())
RC=[list(map(int,input().split())) for _ in range(N)]

G=[[0]*8 for _ in range(8)]

def fmtprt(G):
    print("="*20)
    for g in G:
        print(''.join(map(str,g)))
    print("="*20)

def getcon(r,c):
    pos=[]
    
    direct=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
    
    for d_r,d_c in direct:
        n_r,n_c=r,c  
        while 0<=n_r<8 and 0<=n_c<8:
            if r!=n_r and c!=n_c:
                pos.append((n_r,n_c))
            n_r+=d_r
            n_c+=d_c
    return pos

def verify_q(q,G1):
    debug=False
    #if q==(6, 0, 2, 7, 5, 3, 1, 4):debug=True

    if debug:fmtprt(G1)
    
    for r in range(8):
        c=q[r]
        if ([r,c]) in RC: continue
        if (G1[r][c])!=0:
            if debug:
                fmtprt(G1)
                #print(r,c)
            return False
        G1[r][c]=9
        npos=getcon(r,c)
        for nr,nc in npos:
            if (G1[nr][nc])==9:
                if debug:print(r,c,nr,nc)
                return False
            G1[nr][nc]=1
    return True

for r,c in RC:
    G[r][c]=9
    npos=getcon(r,c)
    # print(npos)
    for nr,nc in npos:
        if G[nr][nc]==0:
            G[nr][nc]=1

JUN=[]
for g in G:
    #print(g)
    t=[]
    for i in range(8):
        if g[i]==0:
            t.append(i)
    JUN.append(t)
for r,c in RC:
    JUN[r]=[c]
# print(JUN)

for r,c in RC:
    JUN[r].append(c)

import itertools
l_p = list(itertools.product(*JUN))

for i in l_p:
    #print(i)
    if len(set(i))!=8: continue
    if (verify_q(i,copy.deepcopy(G))):break
ans=[['.']*8 for _ in range(8)]

for j in range(8):
    ans[j][i[j]]='Q'
    print(''.join(ans[j]))