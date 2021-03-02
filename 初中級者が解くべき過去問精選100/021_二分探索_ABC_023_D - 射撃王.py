'''
N=4
H=[5, 12, 14, 21]
S=[6, 4, 7, 2]
'''

N=int(input())
H=[]
S=[]
for _ in range(N):
    h,s=map(int,input().split())
    H.append(h)
    S.append(s)

INF=1<<60
left=0
right=INF

while right-left>1:
    #print(left,right)
    mid = (left+right)//2
    ok=True
    t=[0]*N
    for i in range(N):
        if mid < H[i]:
            ok=False # —^‚¦‚ç‚ê‚½‚“x‚ª‰Šú‚“x‚æ‚è’á‚¯‚ê‚Î‚¾‚ß
        else:
            t[i]=(mid-H[i])/S[i] # —^‚¦‚ç‚ê‚½‚“x‚É‘Î‚µ‚ÄŒ‚‚¿—Ž‚Æ‚·‚Ì‚É‚©‚©‚é§ŒÀ t[i]–¢–ž‚Ìê‡‚É‚Í‚¤‚¿—Ž‚Æ‚¹‚È‚¢
    t=sorted(t)
    #print(t)
    for i in range(N):
        if (t[i]<i): ok=False
    if ok : right=mid
    else:
        left=mid
    #print(left,right)
print(right)