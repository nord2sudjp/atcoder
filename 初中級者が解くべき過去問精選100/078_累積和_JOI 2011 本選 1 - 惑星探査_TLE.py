import sys
 
def main():
    #input = sys.stdin.readline
 
    #N=4;M=7;Q=1
    #S=['JIOJOIJ','IOJOIJO','JOIJOOI','OOJJIJO']
    #K=[[2,2,3,6]]
 
    N,M=map(int,input().split())
    Q=int(input())
    S=[input() for _ in range(N)]
    K=[list(map(int,input().split())) for _ in range(Q)]
 
 
    m_1=[[[0]*(3) for _ in range(M+1)] for _ in range(N+1)]
 
    l=len(S)
    for a in range(l):
        # ínå`ê}ÇàÍçsÇ∏Ç¬ì«Çﬁ
        s=S[a]
        prv_m=m_1[a]
        cur_m=m_1[a+1]
        for i in range(M):
           cur_m[i+1][0]=cur_m[i][0]+prv_m[i+1][0]-prv_m[i][0]
           cur_m[i+1][1]=cur_m[i][1]+prv_m[i+1][1]-prv_m[i][1]
           cur_m[i+1][2]=cur_m[i][2]+prv_m[i+1][2]-prv_m[i][2]
           if s[i]=='J':
            cur_m[i+1][0]+=1
           elif s[i]=='O':
            cur_m[i+1][1]+=1
           else:
            cur_m[i+1][2]+=1
 
    #print("-"*20)   
    #for t in m_1:
    #    print(t)
 
    for pos in K:
        pl=pos[1]
        pr=pos[3]
        pt=pos[0]
        pb=pos[2]
 
        ans=[0]*3
 
        base=m_1[pb][pr]
        x1=m_1[pt-1][pr]
        x2=m_1[pb][pl-1]
        x3=m_1[pt-1][pl-1]
        ans=[base[i]-x1[i]-x2[i]+x3[i] for i in range(3)]
        print(' '.join(map(str,ans)))        
 
if __name__ == '__main__':
    main()