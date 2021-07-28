# 085 - Multiplication 085

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

N=int(input())

# N=42

l=md(N)

ans=0

for i in l:
    for j in l:
        if N%(i*j)==0:
            k=N/(i*j)
            if i<=j<=k:
                ans+=1

print(ans)