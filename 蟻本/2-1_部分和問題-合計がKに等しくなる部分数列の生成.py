# 合計がKに等しくなる部分数列の生成

#N=4
#A=[1,2,4,7]
#K=13

N=int(input())
*A,=map(int,input().split())
K=int(input())

D=[]

def dfs(n,a):
    if N<=n:
        print(a)
        if sum(a)==K:
            D.append(a)
            return False
        return False

    if dfs(n+1,a): return True 
    if dfs(n+1,a+[A[n]]): return True # 前のステップで数列が出来上がってしまうと、ここは評価されない。

    return False

print(dfs(0,[]))
print(D)