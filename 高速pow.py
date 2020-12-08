def f(n,M):
    if n==0:return 1
    elif n%2==0:
        x=f(n/2,M)
        x*=x
        return x%M
    else:
        x=f((n-1)/2,M)
        x*=x*2
        return x%M


for i in range(1,100):
    print(f(i,10**9+7),pow(2,i,10**9+7))
    
    