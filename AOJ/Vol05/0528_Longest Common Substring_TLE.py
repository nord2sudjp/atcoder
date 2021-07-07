# Python‚Å‚ÍRolling Hash‚Å‰ðŒˆ‚·‚é‚ç‚µ‚¢

# 0528 Common Sub-String

import sys

def fmtprt(DP):
    for d in DP:
        print(d)

def solve(S,T):
    l_S=len(S)
    l_T=len(T)
    DP=[[0]*(l_T+1) for _ in range(l_S+1)]
    ans=0
    for s in range(l_S):
        for t in range(l_T):
            #DP[s+1][t+1]=DP[s][t+1]
            if S[s]==T[t]:
                v=DP[s][t]+1
                DP[s+1][t+1]=v
                if ans<v:ans=v
    #fmtprt(DP)
    return ans
    #return max([max(dp) for dp in DP])
    #return max(DP[-1])
    
# S="ABRACADABRA"
# T="ECADADABRBCRDARA"

# S="UPWJCIRUCAXIIRGL"
# T="SBQNYBSBZDFNEV"

input=sys.stdin.readlines()

l_input=len(input)

for i in range(0,l_input,2):
    S=input[i]
    T=input[i+1]

    print(solve(S,T))
