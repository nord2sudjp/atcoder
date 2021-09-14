# 006 - Smallest Subsequenceiš5j

N,K=map(int,input().split())
S=input()

# N,K=7,3
# S="atcoder"

ans=[]
i=0
while K>0:
    left=i
    right=N-K
    #print(S[left:right+1])
    # select least character from S[left:right+1]
    pos=left
    for j in range(left,right+1):
        if S[pos]>S[j]:
            pos=j
    #print(pos)
    ans.append(S[pos])
    i=pos+1
    K=K-1
    
print(''.join(ans))