i3=lambda : map(int,input().split())
i4=lambda n : list(map(int,input().split()) for _ in range(n))

N,C=i3()
A=i4(N)

events={}
l=len(A)
for i in range(l):
    s,e,c=A[i]
    events[s]=events.get(s, 0)+c
    events[e+1]=events.get(e+1,0)-c

events=sorted(events.items(), key=lambda x: x[0])

ans=0
s=0
pre=0

for event in events:
    ans += min(C,s)*(event[0]-pre)
    s+=event[1]
    pre=event[0]
print(ans)