# 競プロ典型-48
# 部分点は満点より小さく満点の半分より大きい
# この条件により部分点はかならず残りよりも先のステップで消費される

N,K=map(int,input().split())
AB=[list(map(int,input().split())) for _ in range(N)]

# N=4
# K=3
# AB=[[4, 3], [9, 5], [15, 8], [8, 6]]

half=[h for f,h in AB]
rest=[f-h for f,h in AB]


half=[h for f,h in AB]
rest=[f-h for f,h in AB]
half.extend(rest)

half=sorted(half, reverse=True)

print(sum(half[:K]))
