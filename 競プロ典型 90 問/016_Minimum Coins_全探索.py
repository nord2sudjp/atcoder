# https://atcoder.jp/contests/typical90/submissions/22168311

import sys
 
N=int(input())
A,B,C=list(map(int, input().split()))
 
MAXM=10000
ans=float('inf')
for i in range(0,MAXM):
 l=MAXM-i
 if N<i*A:break
 for j in range(0,l):
     if N<(i*A+j*B):break
     k=N-(i*A+j*B) # C�ŕ₤����
     if k%C==0 and 0<=k: # mod�̓}�C�i�X�ł�True�ɂȂ��Ă��܂�
         t=i+j+k//C # ���v�̖���
         if 0<t<10000: # t��0����
           if t<ans:ans=t # ans�ɂ��Ă̓��X�g���g���̂���߂�
print(ans)