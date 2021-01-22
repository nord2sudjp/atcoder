l=[]
while True:
    n,x=map(int,input().split())
    if n==0 and x==0: break
    l.append((n,x))

for n,x in l:
    ans=0
    for h in range(1,n-1):
        for i in range(h+1,n):
            for k in range(i+1,n+1):
                if h+i+k==x: ans+=1
    print(ans)