# 0529 Darts - bisect

from bisect import bisect_right,bisect_left
import sys

def main():
  f = sys.stdin.readline

  while True:

      N,M=map(int,f().split())
      if N==M==0:break
      P=[int(f()) for _ in range(N)]
      P.append(0)

  # N=3
  # M=21
  # P=[16,11,2]

  # N=4
  # M=50
  # P=[3,14,15,9]

      #D=P[:]

      D=[i+j for i in P for j in P if i<=j]

      #TLE D=[P[i]+P[j] for i in range(N+1) for j in range(N+1)]
      #TLE D=[P[i]+P[j] for i in range(N+1) for j in range(N+1) if P[i]+P[j]<=M]
      D.sort()
      #ans=0
      ans=[]
      l_D=len(D)
      for d in D:
          if d>M:continue
          #print(d)
          c=bisect_right(D,M-d)-1
#           c=bisect_left(D,M-d)
#           if c>=l_D:
#               c-=1
#           if D[c]+d>=M:
#               c-=1
          ans.append(D[c]+d)
          #t=D[c]+d
          #if ans<t:ans=t
      print(max(ans))

main()