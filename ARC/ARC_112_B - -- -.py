b,c=map(int,input().split())

s=[0]*4

p=[0]*4

if b>=0:
    s[0]=max((c-2)//2,0)
       # c‚ÌğŒ‚ğŒ©‚é‚±‚Æ
    s[1]=c//2
    s[2]=(c-1)//2
    s[3]=(c-1)//2
    
    p[0]=b+s[0]
    p[1]=b-s[1]
    p[2]=-b+s[2]
    p[3]=-b-s[3]

    if p[1]<=p[3]:
        ans=p[0]-p[1]+1
    elif p[1]<=p[2]:
        ans=p[0]-p[3]+1
    else:
        ans=sum(s)+2
    
else:
    s[0]=c//2
    s[1]=max((c-2)//2,0)
    s[2]=(c-1)//2
    s[3]=(c-1)//2
    
    p[0]=b-s[0]
    p[1]=b+s[1]
    p[2]=-b-s[2]
    p[3]=-b+s[3]
    
    if p[1]>=p[3]:
        ans=p[1]-p[0]+1
    elif p[1]>=p[2]:
        ans=p[3]-p[0]+1
    else:
        ans=sum(s)+2    
print(ans)