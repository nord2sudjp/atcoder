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
        # �����悭�ǂނ���
        #�c�̒�����f(3d) �ŉ��̒�����d�ł��钷���`�̖ʐ�
        ans+=d*d*s 
        d+=s
    print(ans)