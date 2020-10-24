N=int(input())
S=input()

a=0
key=set()
for i in range(N):
    for j in range(i+1,N):
        s=S[i]+S[j]
        if not(s in key):
            a+=len(set(S[j+1:]))
            key.add(s)
print(a)            