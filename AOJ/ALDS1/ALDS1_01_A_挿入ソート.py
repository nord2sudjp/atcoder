N=int(input())
*A,=list(map(int,input().split()))


l=len(A)
for i in range(1,l):
    print(' '.join(map(str,A)))
    key=A[i] # keyはソートされていない値
    j=i-1 # ソートされている配列の最後尾
    while j>=0 and A[j] > key: 
        # すでにソートされている配列は0..i-1
        # 値が大きい場合にはずらしていく
        A[j+1] = A[j]
        # 最初のj=i-1である
        # ずらしていく
        j-=1
    A[j+1]=key
        # ずらし終えたらkeyを設定
print(' '.join(map(str,A)))
