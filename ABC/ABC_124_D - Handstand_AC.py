N,L=map(int,input().split())
A=input()


s=[]

if A[0]=='0':
    s.append(0)

tmp, count = A[0], 1
for i in range(1,len(A)):
    if tmp == A[i]:
        count += 1
    else:
        s.append(count)
        tmp = A[i]
        count = 1
s.append(count) # while‚È‚ç•Ï‰»‚µ‚½Žž“_‚ ‚é‚¢‚Í––’[‚ðŒŸ’m‚Å‚«‚é


if A[-1]=='0':
    s.append(0)

#print(s)

l=len(s)
sums=[0]*(l+1)
for i in range(0,l):
    sums[i+1]=sums[i]+s[i]
#print(sums)


res = 0
l=len(sums)
for left in range(0,len(sums), 2):
    right=left+L*2+1;
    if (right >= l):right=l-1;
    res = max(res, sums[right]-sums[left])
print(res)