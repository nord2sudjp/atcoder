def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
    
    
    
def md(n):
    ld,ud=[],[]
    i=1
    while i*i <= n:
        if n%i==0:
            ld.append(i)
            if i!=n//i:
                ud.append(n//i)
        i+=1
    return ld+ud[::-1]