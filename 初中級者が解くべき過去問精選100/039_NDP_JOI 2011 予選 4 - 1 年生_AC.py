N=int(input())
*S,=map(int,input().split())

DP=[[0]*(21) for _ in range(N+1)]
DP[1][S[0]]=1
for i in range(N-1):
    s=S[i]
    for j in range(21):
        # if j==s: DP[i+1][j]=1
        #      s‚ÍŸ‚ÌsˆÈ~‚Íj-s‚Æj+s‚Åæ‚èˆµ‚í‚ê‚éB
        if 0<=j-s:
            l=DP[i][j-s]
        else:
            l=0
        if j+s<=20:
            r=DP[i][j+s]
        else:
            r=0
        DP[i+1][j]+=l+r 

def fmtdp(DP):
    for dp in DP:
        print(','.join(map(str,dp)))
        
print(DP[N-1][S[-1]])