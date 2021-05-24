# CGL_2_A
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3058807

import sys
from decimal import Decimal


def dot(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def cross(v1,v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
    #https://pcl.solima.net/pyblog/archives/779

    d1x = x2 - x1
    d1y = y2 - y1
    d2x = x4 - x3
    d2y = y4 - y3

    return cross([d1x,d1y],[d2x,d2y])==0
    #return d1x * d2y == d1y * d2x
    # ベクトルa,bの外積の大きさ=0

def is_orthogonal(x1, y1, x2, y2, x3, y3, x4, y4):
    d1x = x2 - x1
    d1y = y2 - y1
    d2x = x4 - x3
    d2y = y4 - y3
    
    return dot([d1x,d1y],[d2x,d2y])==0
#     if d1x*d2x + d1y*d2y == 0:
#         return True
#     else:
#         return False

N=int(input())

for _ in range(N):
    x1, y1, x2, y2, x3, y3, x4, y4=map(int,input().split())
    if is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
        print(2)
    elif is_orthogonal(x1, y1, x2, y2, x3, y3, x4, y4):
        print(1)
    else:
        print(0)
    