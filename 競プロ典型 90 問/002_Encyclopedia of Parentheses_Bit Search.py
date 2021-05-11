#N=10
N=int(input())

ans=[]
for i in range(2**N): 
    t=0
    s=''
    for j in range(N): 
        if (i>>j&1):
            t+=1
            s+='('
        else:
            t-=1
            s+=')'
        if t<0:break
    if t==0:
        ans.append(s)

ans=sorted(ans)

for a in ans:
    print(''.join(a))