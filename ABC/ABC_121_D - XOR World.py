A,B=map(int,input().split())

def oddsolve(a):
    return int(((a+1)/2)%2)

def solve(a):
    if a%2==1:
        return oddsolve(a)
    else:
        return oddsolve(a+1)^(a+1)

print(solve(B) ^ solve(A-1))