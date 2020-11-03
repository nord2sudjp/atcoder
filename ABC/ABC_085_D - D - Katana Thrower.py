f=lambda:map(int,input().split())
N,H=f()
amax=0

A=[]
B=[]
for _ in range(N):
    a,b=f()
    A.append(a)
    amax=max(a,amax)
    B.append(b)

B=sorted(B)
import bisect
t=bisect.bisect_right(B,amax)
B=sorted(B[t:], reverse=True)
lenb=len(B)

c=d=0
while d<H and c<lenb:
    d+=B[c]
    c+=1
z=0
if 0<(H-d):
    z=-(-(H-d)//amax)
    
print(c+z)