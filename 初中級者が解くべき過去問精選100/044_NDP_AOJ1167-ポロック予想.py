#https://www.utakata.work/entry/2015/05/21/140023
#https://kakedashi-engineer.appspot.com/2020/06/13/aoj1167/

import sys

MAXD=1000000+1
DP=[0]*MAXD
DP_O=[0]*MAXD

def main():

    for i in range(MAXD):
        DP[i]=i
        DP_O[i]=i
    n=p=1
    while p<=MAXD:
      if p&1: # mod‚ÌŽæ‚è•û
        for i in range(p,MAXD):
            new = DP[i-p]+1 # •Ï”‚ÍŽg‚¢‚Ü‚í‚µ
            if DP[i] > new:
               DP[i]=new
            new = DP_O[i-p]+1
            if DP_O[i] > new:
               DP_O[i]=new
      else:
        for i in range(p,MAXD):
            new = DP[i-p]+1
            if DP[i] > new: # min‚ÍŽg‚í‚È‚¢
               DP[i]=new

      n+=1
      p=int(n*(n+1)*(n+2)/6)
    ans=[]
    for l in sys.stdin.readlines():
        N=int(l)
        if N==0:break
        ans.append([DP[N],DP_O[N]])
    for a,b in ans:
        print(a,b)

main()


