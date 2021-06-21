# 0100 Sale Result

while True:
    N=int(input())
    if N==0:break
    D={}
    cnt=1
    for _ in range(N):
        e,p,q=map(int,input().split())
        c,total=D.get(e,(-1,0))
        if c==-1:
            c=cnt
        total=total+p*q
        d[e]=[cnt,total]
    print(D)