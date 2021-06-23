INF=float('inf')
finstate = [1,1,1,1,1,1,1,1,1,2,2,2,4,4,4,6,6,6,5,5,5,3,3,3,3,3,3,3,3,3]
D={}
D[tuple(finstate)]=0

def k(comm,p):
    if comm==0:
        p[0],p[1],p[2], p[27],p[28],p[29] = p[27],p[28],p[29], p[0],p[1],p[2]
        p[14], p[15] = p[15], p[14]
        p[18], p[20] = p[20], p[18]
    elif comm==1:
        p[2],p[5],p[8], p[21],p[24],p[27] = p[21],p[24],p[27], p[2],p[5],p[8]
        p[11], p[18] = p[18], p[11]
        p[12], p[14] = p[14], p[12]
    elif comm==2:
        p[6],p[7],p[8], p[21],p[22],p[23] = p[21],p[22],p[23], p[6],p[7],p[8]
        p[12], p[17] = p[17], p[12]
        p[9], p[11] = p[11], p[9]
    elif comm==3:
        p[0],p[3],p[6], p[23],p[26],p[29] = p[23],p[26],p[29], p[0],p[3],p[6]
        p[9], p[20] = p[20], p[9]
        p[15], p[17] = p[17], p[15]
    return p

def dfs(count,p):
    if count>=8:return
    ans=INF
    count=count+1
    for i in range(4):
        k(i,p)
        t=tuple(p)
        if t not in D or D[t]>count:
            D[t]=count
        dfs(count,p)
        k(i,p)
    return
import sys

def main():
    dfs(0,finstate)
    N=int(input())
    I=sys.stdin.readlines()  
    for l in I:
        *x,=list(map(int,l.split()))
        ans=D[tuple(x)]
        print(ans)

main()