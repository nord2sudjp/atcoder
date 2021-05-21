# 034 - There are few types of elements - AC

def solve(N,S,A):
    ans=0
    right=0
    s={}
    cnt=0
    for left in range(N):
        while right<N:
            a=A[right]
            t=s.get(a,0)
            if t=0 and cnt+1>S:
                break
            if t==0: # V‚µ‚¢”‚Ìê‡‚É‚Íí—Ş‚ğ‘‚â‚·
                cnt+=1
            s[a]=t+1
            right=right+1
        t=right-left
        if ans < t:
            ans=t
        #print(s,left,right)
        if right==left:
          right=right+1
        else:
          t=s[A[left]]
          t=t-1
          s[A[left]]=t
          if t==0:
                cnt-=1
    return ans

N,K=map(int,input().split())

*A,=list(map(int,input().split()))
print(solve(N,K,A))
