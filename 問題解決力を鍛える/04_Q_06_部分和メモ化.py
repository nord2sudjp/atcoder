def f(I,W,A): # 最初のI個だけ選んで、Wにすることができるか
    print(DP)
    # f(0,W,A)の場合、0個しか選べないので、答えは必ずFalseになる。
    if (I==0): # 最後まで選択が終わっている
        if W==0: # 選択した結果はWと等しい
            return True
        else:
            return False
    
    if DP[I][W]!=-1:return DP[I][W]
    
    # I-1を選択する
    if f(I-1,W-A[I-1],A):
        DP[I][W]=True
        return True
    
    # I-1を選択しない
    if f(I-1,W,A): 
        DP[I][W]=True
        return True

    # その他
    DP[I][W]=False
    return False


N,W=map(int,input().split())
*A,=list(map(int,input().split()))

DP=[[-1]*(N+10) for _ in range(sum(A)+10)]
DP[0][0]=False
# サブセットに対して適切な合計値はWだけでははなくなる
# これは引き算されていくため
# よってDP[I]だけではなりたたない。

print(f(len(A), W,A))