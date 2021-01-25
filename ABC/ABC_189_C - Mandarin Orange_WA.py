 N=int(input())
 *A,=list(map(int,input().split()))
 ans=0
 for l in range(N):
     cnt=x=A[l]
     r=l+1
     while r<N and a<=A[r]:
             # lは固定している。
             # そのlに対するrはr<lとなった時点で探索をやめている
             # しかし実際にはlとrのすべての組み合わせについてその中での最小値を求めるのが正しい
         cnt+=x # ここは掛け算にできる
         r+=1
     print(l+1,r,A[l],cnt,ans)
     ans=max(ans,cnt)
 print(ans)           