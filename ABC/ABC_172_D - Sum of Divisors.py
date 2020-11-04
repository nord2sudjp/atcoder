N=int(input())
d=[2]*(N+1)
d[1]=1

l=N//2+1
for i in range(2,l):
    s=i+i
    while s<=N:
        # print(i,s)
        d[s]+=1
        # print(i,s)
        s+=i

print(sum([i*d[i] for i in range(1,N+1)]))