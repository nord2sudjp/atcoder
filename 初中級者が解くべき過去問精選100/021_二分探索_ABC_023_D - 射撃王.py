'''
N=4
H=[5, 12, 14, 21]
S=[6, 4, 7, 2]
'''

N=int(input())
H=[]
S=[]
for _ in range(N):
    h,s=map(int,input().split())
    H.append(h)
    S.append(s)

INF=1<<60
left=0
right=INF

while right-left>1:
    #print(left,right)
    mid = (left+right)//2
    ok=True
    t=[0]*N
    for i in range(N):
        if mid < H[i]:
            ok=False # 与えられた高度が初期高度より低ければだめ
        else:
            t[i]=(mid-H[i])/S[i] # 与えられた高度に対して撃ち落とすのにかかる制限 t[i]未満の場合にはうち落とせない
    t=sorted(t)
    #print(t)
    for i in range(N):
        if (t[i]<i): ok=False
    if ok : right=mid
    else:
        left=mid
    #print(left,right)
print(right)

## OK
Time: 1 2 3 4 5
撃ち落とすタイミング: 1 3 4 5 9

## No
Time: 1 2 3 4 5
撃ち落とすタイミング: 1 1 2 3 4