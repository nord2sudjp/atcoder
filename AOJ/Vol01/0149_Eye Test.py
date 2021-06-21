# 0149 Eye Test

import sys

l=sys.stdin.readlines()

ans=[[0,0] for _ in range(4)]

for i in l:
    l,r=map(float,i.split())
    
    if 1.1<=l:
        ans[0][0]+=1
    elif 0.6 <= l <1.1:
        ans[1][0]+=1
    elif 0.2<=l<0.6:
        ans[2][0]+=1
    else:
        ans[3][0]+=1

        
    if 1.1<=r:
        ans[0][1]+=1
    elif 0.6 <= r <1.1:
        ans[1][1]+=1
    elif 0.2<=r<0.6:
        ans[2][1]+=1
    else:
        ans[3][1]+=1

for a in ans:
    print(' '.join(map(str,a)))