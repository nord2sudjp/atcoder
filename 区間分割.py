N=[1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
i=0;
l=len(N)
res=0
while i<l:
    if (N[i] == 0):
        i+=1# 0ならそのまま進む
    else:
        res+=1 # 新しい区間の始まり
        while i<l and 0<N[i]:
            i+=1 #区間の終わりまで一気に
print(res)