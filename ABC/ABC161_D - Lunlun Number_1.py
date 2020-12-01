K=int(input())

a=[]
a=list(range(1,10))

ans=0
while True:
    if (K<=len(a)):
        ans=a[K-1]
        break
    K-=len(a)
    old=[]    
    a,old=old,a
    
    for x in old:
        for i in range(-1, 2):
            d=x%10+i # ––”ö‚Ì’l
            if (d<0 or d>9): continue
            nx = x*10+d
            a.append(nx)
print(ans)