# 0652  Social Game

import math
A,B,C=map(int,input().split())

# A=3
# B=0
# C=10

t=C//(7*A+B)
ans=7*t
C=C-t*(7*A+B)

if C<=7*A:
    ans+=math.ceil(C/A)
else:
    ans+=7
print(ans)