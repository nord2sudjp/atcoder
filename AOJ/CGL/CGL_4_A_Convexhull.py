# CGL_4_A
# Convex hull
# http://kb84tkhr.hatenablog.com/entry/2019/08/08/211442

from decimal import *
getcontext().prec = 15

        
def dot(v1,v2):
    return Decimal(v1[0])*Decimal(v2[0])+Decimal(v1[1])*Decimal(v2[1])

def cross(v1,v2):
    return Decimal(v1[0])*Decimal(v2[1])-Decimal(v1[1])*Decimal(v2[0])


def half_hull(P):
    N=len(P)
    S = []
    # �ŏ��̂Q�_��ǉ�����
    S.append(P[0])
    S.append(P[1])
    
    # ���ׂĂ̓_�ɂ��ēǂݍ���ł���
    for i in range(2, N):
        # S�ɂQ�ȏ�̓_������ꍇ�ɂ͍��������悤�Ƃ��Ă���_�ɂ��ĕ]�������遨�]���̌��ʂƂ���
        # Pop����B
        # S����ɂȂ�A�������͏����𖞂���S[-1]�ɂȂ�����A�����ē_��ǉ�����
        while len(S) > 1:
            v1=[p1-p2 for p1,p2 in zip(S[-1],S[-2])]
            v2=[p1-p2 for p1,p2 in zip(P[i],S[-1])]
            if cross(v1,v2) >= 0:
                break
            S.pop()
        S.append(P[i])
    return S

def convex_full(P):
    return half_hull(sorted(P, key=lambda p: (p[1], p[0])))[:-1] + half_hull(sorted(P, key=lambda p: (p[1], p[0]), reverse=True))[:-1]

N=int(input())
P=[list(map(int,input().split())) for _ in range(N)]

A=convex_full(P)

print(len(A))
for p in A:
  print(' '.join(map(str,p)))