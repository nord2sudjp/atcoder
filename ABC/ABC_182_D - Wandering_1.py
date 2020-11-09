N=int(input())
*A,=map(int,input().split())

ans=0
s=b=mx_b=0
for i in range(N):
    b+=A[i] # i段目におけるΣAを求める
    mx_b=max(mx_b,b)
    ans=max(ans, s+mx_b)
    s+=b # sは次の段のスタート、これはi段目におけるbをスタート地点に足した値
    print(b,s)

print(ans)