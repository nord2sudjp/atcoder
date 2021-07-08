# 0654 Circle Cross Stamps

N=int(input())
S=input()

#S="OXXOX"
T=[]
l_S=len(S)
cur=0
ans=0
while cur<l_S:
    #print(S[cur])
    if cur<l_S-1 and S[cur]=='O' and S[cur+1]=='X':
        cur+=2
        ans+=1
    else:
        T.append(S[cur]) 
        cur+=1
#print(ans,T)
S=T
l_S=len(S)
cur=0
while cur<l_S:
    #print(S[cur])
    if cur<l_S-1 and S[cur]=='X' and S[cur+1]=='O':
        cur+=2
        ans+=1
    else:
        T.append(S[cur]) 
        cur+=1
print(ans)