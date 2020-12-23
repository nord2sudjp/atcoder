def rle(s):
    ans=[]
    tmp, count = s[0], 1
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans.append(count)
            tmp = s[i]
            count = 1
    ans.append(count)
    return ans


#N=14
#L=2
#A="11101010110011"

N,L=map(int,input().split())
A=input()

s=rle(A)
lr=len(s)
if A[0]=='0':
    cur=ans=sum(s[:2*L])
    l=1
    r=2*L-1
    while r<lr:
        t=cur-s[l-2]-s[l-1]+s[r]+s[r-1]
        ans=max(t,ans)
        cur=t
        l+=2
        r+=2
else:
    cur=ans=sum(s[:2*L+1])
    l=2
    r=2*L+2
    while r<lr:
        t=cur-s[l-2]-s[l-1]+s[r]+s[r-1]
        ans=max(t,ans)
        cur=t
        l+=2
        r+=2

print(ans)