def mpow(n,M):
    if n==0:return 1
    elif n%2==0:
        x=f(n/2,M)
        x*=x
        return x%M
    else:
        x=f((n-1)/2,M)
        x*=x*2
        return x%M
