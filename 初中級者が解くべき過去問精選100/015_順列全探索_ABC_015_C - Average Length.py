N=int(input())
X=[list(map(int,input().split())) for i in range(N)]
print(2/N*sum([sum([(l-m)**2for l,m in zip(X[i],X[j])])**0.5for j in range(N) for i in range(N) if i<j ]))