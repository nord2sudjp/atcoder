def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp
            tmp = s[i]
            count = 1
    ans += tmp
    return ans
N,K=map(int,input().split())
S=input()

all=N-1
unluck=len(rle(S))-1
unluck-=2*K

print(min(all-unluck, all))