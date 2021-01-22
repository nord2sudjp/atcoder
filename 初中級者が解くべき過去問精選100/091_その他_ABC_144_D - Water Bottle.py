a,b,x=map(int,input().split())
 
import math
 
S=x/a
 
if S<a*b/2:
  y=b
  x=2*S/b
else:
  y=(a*b-S)*2/a
  x=a
print(math.degrees(math.atan2(y,x)))