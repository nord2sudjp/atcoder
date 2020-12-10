S=input()

ans=False

if len(S)==1:
    if int(S)==8:ans=True
elif len(S)==2:
    if int(S)%8==0:
        ans=True
    else:
        S=S[1]+S[0]
        if int(S)%8==0:
            ans=True
else:
    x=[0]*10
    for s in S:
        x[int(s)]+=1
    
    for i in range(104,1000,8):
        y=[0]*10
        si=str(i)
        for j in si:y[int(j)]+=1

        ans=all(x[i]>=y[i] for i in range(10))
        if ans: break

print('Yes' if ans else 'No')
