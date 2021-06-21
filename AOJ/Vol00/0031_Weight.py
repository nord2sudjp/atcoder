# Volume0-0031 Weight
import math
import sys


l=sys.stdin.readlines()

for N in l:
    ans=[]
    while 0<N:
        s=int(math.log2(N))
        ans.append(s)
        N=N-2**s
    ans=ans[::-1]
    ans=map(str,list(map(lambda x:2**x, ans)))
    print(' '.join(ans))