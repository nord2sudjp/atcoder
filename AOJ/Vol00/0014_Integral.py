# 14 Integral

S=[]
import sys
for l in sys.stdin.readlines():
    S.append(int(l))

# S=[20,10]

for s in S:
    d=s
    ans=0
    while d<=600-s:
        #ans+=d*d*d
        # –â‘è‚ð‚æ‚­“Ç‚Þ‚±‚Æ
        #c‚Ì’·‚³‚ªf(3d) ‚Å‰¡‚Ì’·‚³‚ªd‚Å‚ ‚é’·•ûŒ`‚Ì–ÊÏ
        ans+=d*d*s 
        d+=s
    print(ans)