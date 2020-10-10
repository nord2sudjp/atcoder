f=lambda:map(int,input().split())
#N=int(input())
#*S,=f()
#*T,=f()

N=5
S=[1,2,4,8,6]
T=[3,5,7,10,9]

j=[]
for s,t in zip(S,T):
   j.append((s,t)) 

from operator import itemgetter
j.sort(key=itemgetter(1))
a=0
c=0 # 現在の時間 or 仕事をしていない時間
for s,t in j:
    print(c,s,t,"Select" if c<s else "Ignore")
    if (c<s): # Jobの開始時間がtより大きい場合にはこの仕事を実行できる。
        a+=1
        c=t # 次に空くタイミングは選択したjobの終了時間
print("Total:",a)