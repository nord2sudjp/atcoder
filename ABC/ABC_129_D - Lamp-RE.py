def f(S,R):
    p=0
    l=len(R)
    b=[0]*len(S)
    for c in range(0,l,2):
        #print(p,R[c+1],R[c])
        ri=int(R[c+1])
        if R[c] != '#':
            for i in range(p,p+ri):
                b[i]=ri
        p+=ri
    return b


def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp+str(count)
            tmp = s[i]
            count = 1
    ans += tmp+str(count)
    return f(s,ans)   


H,W=map(int,input().split())
A=[input() for _ in range(H)]


bx=[]

for a in A:
    bx.append(rle(a))
    
l = [list(x) for x in zip(*A)]
by=[]
for i in l:
    by.append(rle(i))
by = [list(x) for x in zip(*by)]

p=(0,0)
m=0
for h in range(H):
    for w in range(W):
        if m < bx[h][w]+by[h][w]:
            p=(h,w)
            m=bx[h][w]+by[h][w]
            # print(h,w,bx[h][w],by[h][w])

print(m-1)