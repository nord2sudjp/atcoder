from math import gcd
A,B=map(int,input().split())

def s(n):
    l=[]
    limit=int(n**0.5)+1
    for i in range(2,limit+1):
        while n%i==0:
            l.append(i)
            n=n//i
    if n>1:l.append(n)
    return(l)
        
g=gcd(A,B)
print(len(set(s(g)))+1)