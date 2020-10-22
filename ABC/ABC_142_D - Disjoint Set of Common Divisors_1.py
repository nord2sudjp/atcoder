# TLE

def md(n):
    ld,ud=[],[]
    i=1
    while i*i <= n:
        if n%i==0:
            ld.append(i)
            if i!=n//i:
                ud.append(n//i)
        i+=1
    return ld+ud[::-1]

def s(k):
    f=0
    if k%2==0 and k!=2:return False
    for d in range(2, k//2):
        if k%d == 0:return False
    return True

A,B=map(int,input().split())

x=set(md(A))
y=set(md(B))
x&=y
x=list(x)


print(len([i for i in x if s(i)]))