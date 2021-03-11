N,M=map(int,input().split())
Q=int(input())
S=[input() for _ in range(N)]
K=[list(map(int,input().split())) for _ in range(Q)]
 
 
LD={"J":0, "O":1, "I":2}
 
m_1=[] # 全体の地形図
m_1.append([[0]*(3) for _ in range(M+1)])
 
for s in S:
    # 地形図を一行ずつ読む
    m=[[0]*(3) for _ in range(M+1)]
    for i in range(M):
       for j in range(3):
        m[i+1][j]=m[i][j]+m_1[-1][i+1][j]-m_1[-1][i][j]
       m[i+1][LD[s[i]]]=m[i+1][LD[s[i]]]+1
    m_1.append(m)
 
#for t in m_1:
#    print(t)
    
def f(pos):
    pl=pos[1]
    pr=pos[3]
    pt=pos[0]
    pb=pos[2]
 
    ans=[0]*3
    
    base=m_1[pb][pr]
    x1=m_1[pt-1][pr]
    x2=m_1[pb][pl-1]
    x3=m_1[pt-1][pl-1]
    for i in range(3):
        ans[i]=base[i]-x1[i]-x2[i]+x3[i]
    print(' '.join(map(str,ans)))
    
for k in K:
    f(k)