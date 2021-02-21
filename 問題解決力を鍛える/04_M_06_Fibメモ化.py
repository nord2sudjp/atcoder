def fib(N):
    if N==0:return 0
    elif N==1:return 1
    if mem[N]!=-1:return mem[N]
    res= fib(N-1)+fib(N-2)
    mem[N]=res
    return res

S=35
mem=[-1]*(S+1)

fib(S)