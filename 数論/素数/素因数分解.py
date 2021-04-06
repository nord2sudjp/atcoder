# https://nagiss.hateblo.jp/entry/2019/07/01/185421
# ‘fˆö”•ª‰ğ
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

#
def s(n):
    l=[]
    limit=int(n**0.5)+1
    for i in range(2,limit+1):
        while n%i==0:
            l.append(i)
            n=n//i
    if n>1:l.append(n)
    return(l)
s(24)