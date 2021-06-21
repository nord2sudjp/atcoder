# Volume2-0241 Quaternion Multiplication

#l1=[1,2,3,4]
#l2=[7,6,7,8]

while True:
    N=int(input())
    if N==0:break
    
    for _ in range(N):
        *t,=list(map(int,input().split()))
        l1=t[0:4]
        l2=t[4:]

        s=[x*y for x in l1 for y in l2]
        ans=[0]*4 #1,i,j,k

        ans[0]+=s[0]
        ans[1]+=s[1]+s[4]
        ans[2]+=s[2]+s[8]
        ans[3]+=s[3]+s[12]

        ans[0]+=-1*s[5]-1*s[10]-1*s[15]
        ans[1]+=s[11]-1*s[14]
        ans[2]+=-1*s[7]+s[13]
        ans[3]+=s[6]-1*s[9]

        print(' '.join(map(str,ans)))