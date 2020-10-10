f=lambda:map(int,input().split())
# N,R=f()
# *X,=sorted(f())

N=6
R=10
X=sorted([1,7,15,20,30,50])

i=ans=0

while i<N: #iはNより小さい範囲で進める
 print(i)
 s=X[i] # sはRによりカバーされていない点の集合のうち、最も小さい（左にある）点
 i+=1 # 点と点の間がRより大きい場合にはそもそも成り立たない→これは問題の条件として無視できる
 while i<N and X[i]<=s+R:i+=1 # sからRの範囲内でiを進める
   # この処理がおわるとiはs+Rの範囲を一つだけ越えている。
 p=X[i-1] # 次の点
 while i<N and X[i]<=p+R:i+=1
   # pから次のrを越える点まで進む。そしたら次のループに入る
 ans+=1
print(ans)