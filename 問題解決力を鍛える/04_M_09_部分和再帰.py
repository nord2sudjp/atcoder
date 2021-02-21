def f(I,W,A): # 最初のI個だけ選んで、Wにすることができるか
    # f(0,W,A)の場合、0個しか選べないので、答えは必ずFalseになる。
    if (I==0): # 最後まで選択が終わっている
        if W==0: # 選択した結果はWと等しい
            return True
        else:
            return False
    
    # I-1を選択する
    if f(I-1,W-A[I-1],A): return True
    
    # I-1を選択しない
    if f(I-1,W,A): return True

    # その他
    return False


N,W=map(int,input().split())
*A,=list(map(int,input().split()))

print(f(len(A), W,A))