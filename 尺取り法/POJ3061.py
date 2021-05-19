def solve(N,S,A):
    ans=N+1
    left=right=0
    sum=0
    while True:
        while right<N and sum < S:
            sum=sum+A[right]
            right=right+1
        if sum<S:break
        t=right-left
        if t < ans:
            ans=t
        sum=sum-A[left]
        left=left+1
    # print(ans)
    if ans>N+1:
        ans=0
    return ans

print(solve(10,15,[5,1,3,5,10,7,4,9,2,8]))
print(solve(5,11,[1,2,3,4,5]))