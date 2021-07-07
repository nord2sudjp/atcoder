# 0587 Tunnel

T=int(input())
S=int(input())

ans=S
for _ in range(T):
    a,b=map(int,input().split())
    S=S+a-b
    if S<0:
      ans=0
      break
    if ans<S:
        ans=S
print(ans)