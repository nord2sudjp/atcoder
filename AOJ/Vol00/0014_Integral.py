# 14 Integral

S=[]
import sys
for l in sys.stdin.readlines():
    S.append(int(l))

# S=[20,10]

for s in S:
    d=s
    ans=0
    while d<=600-s:
        #ans+=d*d*d
        # 問題をよく読むこと
        #縦の長さがf(3d) で横の長さがdである長方形の面積
        ans+=d*d*s 
        d+=s
    print(ans)