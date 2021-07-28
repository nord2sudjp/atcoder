def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime

N,K=map(int,input().split())

N=N+1
S=makePrimeChecker(N)

D=set()
for i,s in enumerate(S):
    if s:
        D.add(i)

        
DP=[0]*N        
for d in D:
    od=d
    while d<N:
        DP[d]+=1
        d=d+od

print(sum([1 for i in DP if i>=K]))