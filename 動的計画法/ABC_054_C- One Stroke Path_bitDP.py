f=lambda:map(int,input().split())
N,M=f()
 
A=[]
for i in range(M):
  a,b=f()
  A.append([a-1,b-1])
 
A=[*A,*[[y,x] for x,y in A]]
A=set(list(map(tuple,A)))
 
 
#N=3
#M=3
#A=[[1,2], [1, 3], [2, 3]]
 
 
def bit_dp(N,A):
    #print(A)
    dp = [[0]*N for i in range(1 << N)]
    #dp(S, v) = (���_0����o�����A�W��S�Ɋ܂܂�钸�_��S�ĖK���path�̂������_v���Ō�ɂȂ�悤��path�̑���)
 
    dp[1][0] = 1     
    # dp({0}, 0) = 1 �Ə���������
 
    for S in range(1 << N): # 1<<N=2**N
        for v in range(N):
            # v �� S �Ɋ܂܂�Ă��Ȃ��Ƃ��̓p�X����
            if (S & (1 << v)) == 0:
                continue
 
            # sub = S - {v}
            sub = S ^ (1 << v) # v�����}�X�N����
 
            for u in range(N):
                # sub �� u ���܂܂�Ă���A���� u �� v ���ӂŌ��΂�Ă���
                if (sub & (1 << u)) and len(A&{(u,v)})==1:
                      #print(u,v,A&{(u,v)},dp[sub][u])          
                      dp[S][v] += dp[sub][u]
 
    ans = sum(dp[(1 << N) - 1][u] for u in range(1, N))
    # �� dp({0,1,2,...,N-1},u))
    return ans
ans=bit_dp(N,A)
print(ans)    