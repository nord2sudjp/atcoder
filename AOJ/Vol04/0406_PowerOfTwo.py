# 0406 Power of Two
N=int(input())

ans=0
while N>=2:
    N=N/2
    ans+=1
print(2**ans)