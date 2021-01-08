# https://atcoder.jp/contests/abc145/submissions/10775904
def comb(n,r,mod):
    # n‚©‚çr’Ê‚è‚ğ‘I‘ğ‚·‚é
    # mod‚Í‘f”‚Å‚ ‚é‚±‚Æ
    if n<r:return 0
    k=min(r,n-r)
    C=1
    for i in range(1,k+1):
        C=(C*(n+1-i)*pow(i,mod-2,mod))%mod
    return C



# 
def comb_cal(n):
    s=1
    m=0
    for i in range(n):
        s*=2
        m+=s-1
        #print(s-1)
    return((s-1,m))

i,j=comb_cal(3)
print(i,j)

'''
1: 1 : 1
2: 2 1 : 3
3: 3 3 1 : 7
4: 4 6 4 1 : 15
5: 5 10 10 5 1 : 31
6: 6 15 20 15 6 1 : 63
7: 7 21 35 35 21 7 1 : 127
8: 8 28 56 70 56 28 8 1 : 255
9: 9 36 84 126 126 84 36 9 1 : 511
1013
'''
