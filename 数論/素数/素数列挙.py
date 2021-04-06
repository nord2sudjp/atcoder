# nまでの自然数が素数かどうかを表すリストを返す
def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime
    
    
# AOJ vol00:0009
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009
def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime

MAX=1000000
x=makePrimeChecker(MAX)

y=[0]*MAX
for i in range(1,MAX):
    y[i]=y[i-1]+x[i]

#print(y[0:10])

import sys
for l in sys.stdin.readlines():
    print(y[int(l)])