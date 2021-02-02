# https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24)


# https://nagiss.hateblo.jp/entry/2019/07/01/185421
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
    
    
def s(l):
    n=0
    for k in range(2,l+1):
        f=0
        if k%2==0 and k!=2:continue
        for d in range(2, k//2):
            if k%d == 0:
                f+=1
        if f==0:
            n+=1
    return n