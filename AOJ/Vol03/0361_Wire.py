# Volume3-0361 Wire
import math
x,y=map(int,input().split())
g=math.gcd(x,y)
print(int(g*(x/g+y/g)-(g-1)))