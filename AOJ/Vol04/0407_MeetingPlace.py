# 0407 Meeting Place
N=int(input())
*X,=map(int,input().split())
maxx=max(X)
minx=min(X)

p=(maxx+minx)//2

ans=0

for x in X:
    ans=abs(maxx-p)
    if ans<abs(minx-p):
        ans=abs(minx-p)
print(ans)