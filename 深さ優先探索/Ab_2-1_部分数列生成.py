# •”•ª”—ñ‚Ìì¬

# N=4
# A=[1,2,4,7]

N=int(input())
*A,=map(int,input().split())

D=[]

def dfs(n,a):
    if N<=n:
        print(a)
        return False

    dfs(n+1,a)
    dfs(n+1,a+[A[n]])

    return False

print(dfs(0,[]))
