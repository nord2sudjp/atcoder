#
# TLE
# set‚É‚·‚é‚Ì‚ð–Y‚ê‚Ä‚¢‚½¨ if ‚Å in‚Í‚©‚È‚ç‚¸set


import bisect

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]
i7=lambda n : [tuple(map(int,input().split())) for _ in range(n)]

INF=float('inf')

N=i2()
M=sorted(i5(N))

# N=6
# M=[[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

s_M=set([tuple(m) for m in M])

ans=0
for p1 in range(N):
    rt=bisect.bisect_left(M,[M[p1][0]+1,M[p1][1]+1])
    for p2 in range(rt,N):
        mp1=M[p1]
        mp2=M[p2]
        if mp1[1]>=mp2[1]:continue
        if (mp1[0],mp2[1]) in s_M and (mp2[0],mp1[1]) in s_M:
            #print(M[p1],p2)
            ans=ans+1
print(ans)
    




#
i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

N=i2()
M=i5(N)

# N=6
# M=[[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]

d1={}
for m in M:
    t=d1.get(m[0],[])
    t.append(m[1])
    d1[m[0]]=t
    
keys=sorted(d1.keys())
l_keys=len(keys)

ans=0
for k1 in range(l_keys):
    for k2 in range(k1+1,l_keys):
        ys1=d1.get(keys[k1],[])
        ys2=d1.get(keys[k2],[])
        #ys1=d1[k1] #RE
        #ys2=d1[k2] #RE
        

        l_ys1=len(ys1)
        for y1 in range(l_ys1):
            for y2 in range(y1+1,l_ys1):
                if ys1[y1] in ys2 and ys1[y2] in ys2:
                    ans=ans+1
print(ans)
s