# ‘f””»’è
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

# ‘f””»’è
x=99
print(all(1<=x%i for i in range(2,int(x**.5)+1)))


# Next prime‚ğ‹‚ß‚é
while any(x%i<1 for i in range(2,int(x**.5)+1)): x+=1
https://atcoder.jp/contests/abc149/submissions/14499653