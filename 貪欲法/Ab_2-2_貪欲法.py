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
c=0 # ���݂̎��� or �d�������Ă��Ȃ�����
for s,t in j:
    print(c,s,t,"Select" if c<s else "Ignore")
    if (c<s): # Job�̊J�n���Ԃ�t���傫���ꍇ�ɂ͂��̎d�������s�ł���B
        a+=1
        c=t # ���ɋ󂭃^�C�~���O�͑I������job�̏I������
print("Total:",a)