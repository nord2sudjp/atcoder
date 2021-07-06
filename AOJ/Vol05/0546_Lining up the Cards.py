# 0546 Lining up the cards

import itertools


f = lambda : int(input())
# N=4
# K=2
# A=[1,2,12,1]

while True:
    N=f()
    K=f()
    if N==K==0:break
    A=[f() for _ in range(N)] 
    ANS=set()

    per=itertools.permutations(A,K)

    for i in per:
        ANS.add(''.join(map(str,i)))

    print(len(ANS))