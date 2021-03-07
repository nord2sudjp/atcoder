# DP[S][v]: ����v�ɂ���B���ł�S�͖K�ꂽ���ƂɂȂ��Ă���B
# �c��̂��ׂĂ̒��_��K���0�ɖ߂�Ƃ��̃R�X�g

#print(2**5) # 32
#print(1<<5) # 32

def rec(S,v):
    if DP[S][v]>=0:
        # DP[S][v]!=-1�̏ꍇ���łɌv�Z����Ă���
        return DP[S][v]

    if (S==(1<<V)-1 and v==0):
        # 1<<n  = 100000
        # 1<<n-1=  11111
        DP[S][v]=0
        return 0 # ����0�ɂ��āAS������Ă����Ƃ��ɉ�邽�߂ɕK�v�ȃR�X�g=0
        
    res=float('infinity')
    for u in range(V):
        if not(S>>u & 1): # u���W���Ɋ܂܂�Ă��Ȃ��ꍇ
            # u�Ɉړ�����
            
            #print(S,v,u)

            res = min(res, rec(S|1<<u,u) + G[v][u])
            # num1 = 0b0101; bin(1<<3)
            # bin(num1 | 1<<3)
            # '0b1101'
    DP[S][v]=res
    return res

INF=float('infinity')
#G=[[0,3,INF,4,INF],[INF,0,5,INF,INF],[4,INF,0,5,INF],[INF,INF,INF,0,3],[7,6,INF,INF,0]]

V,E=map(int,input().split())

G=[[INF]*V for _ in range(V)]

for _ in range(E):
    s,t,c=map(int,input().split())
    G[s][t]=c

MAX_V=V+1

D=[[0]*MAX_V for _ in range(MAX_V)]
DP=[[-1]*MAX_V for _ in range(2**MAX_V)]

ans=rec(0,0)
print( -1 if ans == INF else ans)
