def s(n):
    l=[]
    limit=int(n**0.5)+1
    for i in range(2,limit+1):
        while n%i==0:
            l.append(i)
            n=n//i
    return(l)
        
