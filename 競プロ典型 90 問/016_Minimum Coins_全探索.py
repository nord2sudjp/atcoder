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
     k=N-(i*A+j*B) # Cで補うお金
     if k%C==0 and 0<=k: # modはマイナスでもTrueになってしまう
         t=i+j+k//C # 合計の枚数
         if 0<t<10000: # tは0より大
           if t<ans:ans=t # ansについてはリストを使うのをやめる
print(ans)