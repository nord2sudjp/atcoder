# 0270 Modular Query
import bisect
import sys

def solve(q,C,MAXC):
    ans=0
    i=1
    while q*i<=MAXC:
        s=bisect.bisect_left(C,q*i)
        #print(q,i,q*i,s,C[s-1])
        if s==0:
            i=i+1
            continue # TLE‚É‚È‚éê‡‚É‚ÍLoop‚µ‚Ä‚¢‚é‚©‚à
        t=C[s-1]%q
        if t>ans:
            ans=t
        i=i+1
    t=MAXC%q
    if t>ans:ans=t
    return ans
    

N,Q=map(int,input().split())
*C,=list(map(int,input().split()))

# N=3
# C=[9,3,8]

C=sorted(C)
MAXC=C[-1]

# q=5
# print(solve(q,C,MAXC))

input=sys.stdin.readlines()
for _ in input:
    print(solve(int(_),C,MAXC))