# 082 - Counting Number

import math
from decimal import *

MOD=10**9+7
L,R=map(int,input().split())


#ans=(R-L+1)*(L+R)/2
#print(int(ans%MOD))

ans=0
S=T=0
while T!=R:
    S=L
    #T=min(10**(int(math.log(L,10))+1)-1,R)
    #length=int(math.log(L,10))+1
    #
    # log‚Í¸“x‚ªˆ«‚¢‚Ì‚Ålog10‚ğ—˜—p‚·‚é
    # => ‚±‚ê‚àŒë·‚ª‚ ‚é‚Ì‚Å•¶š—ñ‚Æ‚µ‚ÄŒvZ‚·‚é
    #length=int(math.log10(L))+1
    length=len(str(L))
    T=min(10**(int(math.log10(L))+1)-1,R)
    #print(L,R,S,T,length,(length*(T-S+1)*(S+T)//2))
    ans+=length*(T-S+1)*(S+T)//2%MOD
    L=T+1
print(ans%MOD)
    