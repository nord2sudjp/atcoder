# 018 - Statue of Chokudai

import math 

T=int(input())
L,X,Y=map(int,input().split())
Q=int(input())

# T=4
# L=2
# X=1
# Y=1
# Q=1

for _ in range(Q):
    e=int(input())
    y1=-1*L/2*math.sin(2*math.pi*e/T)
    z1=L/2-L/2*math.cos(2*math.pi*e/T)
    
    width=(X**2 + (Y-y1)**2)**0.5
    print(math.degrees(math.atan2(z1,width)))
