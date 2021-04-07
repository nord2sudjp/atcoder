import math

a,b,C=map(int,input().split())

S=0.5*a*b*math.sin(math.radians(C))
print(S)
print((a**2+b**2-2*a*b*math.cos(math.radians(C)))**0.5+a+b)
print(2*S/a)s