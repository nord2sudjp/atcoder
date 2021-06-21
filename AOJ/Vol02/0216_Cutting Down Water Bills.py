# 0216 Cutting Down Water Bills

while True:
    N=int(input())
    if N==-1: break
    ans=0
    if N>10:
        ans+=10*1150
        N=N-10
    else:
        ans+=N*1150
        N=0
    
    if N>10:
        ans+=10*125
        N=N-10
    else:
        ans+=N*125
        N=0
        
    if N>10:
        ans+=10*140
        N=N-10
    else:
        ans+=N*140
        N=0
    ans+=N*160
    print(ans)