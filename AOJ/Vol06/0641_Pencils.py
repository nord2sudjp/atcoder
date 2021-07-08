# 0641 Pencils
import math

N,A,B,C,D = map(int,input().split())

x=math.ceil(N/A)*B
y=math.ceil(N/C)*D

print(min(x,y))