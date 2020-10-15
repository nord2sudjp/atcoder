S=input()
L=len(S)
d=[0]*L
s=e=r=l=0
 
i=0
while i<L+1:
    if i==L or l!=0 and S[i]=='R':
        # print(s,r,l,e)
        diff=e-s
        if diff%2==0:
            odd=diff//2
            even=diff//2+1
        else:
            odd=even=diff//2+1
        if r%2==0:
            d[s+r-1]=odd
            d[s+r]=even
        else:
            d[s+r-1]=even
            d[s+r]=odd
        s=i
        r=1
        l=e=0
    elif S[i]=='R':
        r+=1
    else:
        l+=1
    e=i
    i+=1
print(' '.join(map(str,d)))
S=input()
L=len(S)
d=[0]*L
s=e=r=l=0

i=0
while i<L+1:
    if i==L or l!=0 and S[i]=='R':
        # print(s,r,l,e)
        diff=e-s
        if diff%2==0:
            odd=diff//2
            even=diff//2+1
        else:
            odd=even=diff//2+1
        if r%2==0:
            d[s+r-1]=odd
            d[s+r]=even
        else:
            d[s+r-1]=even
            d[s+r]=odd
        s=i
        r=1
        l=e=0
    elif S[i]=='R':
        r+=1
    else:
        l+=1
    e=i
    i+=1
print(' '.join(map(str,d)))
