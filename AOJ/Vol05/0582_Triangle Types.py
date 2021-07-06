# 0582 Triangle Types

def isTriangle(a,b,c):
    return a+b>c and b+c>a and c+a>b

def triangle_type(a,b,c):
    # 1 a2=b2+c2 ‚È‚ç’¼ŠpOŠpŒ`
    # 2 a2<b2+c2 ‰sŠpOŠpŒ`
    # 3 a2>b2+c2 ‚È‚ç“İŠpOŠpŒ`
    # -1 OŠpŒ`‚Å‚Í‚È‚¢
    
    t=sorted([a,b,c])
    a,b,c=t[2],t[0],t[1]
    
    if not(isTriangle(a,b,c)):
        return -1
    if a**2 < b**2+c**2:
        return 2
    elif a**2 == b**2+c**2:
        return 1
    else:
        return 3

ans=[0]*4
while True:
    a,b,c=map(int,input().split())
    t=triangle_type(a,b,c)
    #print(a,b,c,t)
    if t==-1:break
    ans[0]+=1
    ans[t]+=1

print(' '.join(map(str,ans)))
    
    