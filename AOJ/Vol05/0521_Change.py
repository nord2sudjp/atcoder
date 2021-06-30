import sys

C=[500,100,50,10,5,1]
l=sys.stdin.readlines()

for i in l:
    t=int(i)
    if t==0:
        break
    
    ans=0
    o=1000-t
    
    for c in C:
        ans+=o//c
        o=o%c
        
    print(ans)    