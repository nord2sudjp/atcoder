def RepeatSquaring(N,P,M):
    # N^P mod M
    
    if P==0: return 1 
    if P%2==0:
        t=RepeatSquaring(N,P//2,M)
        return (t*t)%M
    else:
        return N*RepeatSquaring(N, P-1, M)

print(RepeatSquaring(19,450,1000000007))
print(pow(19, 450, 1000000007))