def mcomb(n,a,mod):
 x=y=1
 for i in range(1, a+1):
   x = x * (n-i+1) % mod
   y = (y * i) % mod
 da = ((x % mod) * (pow(y, mod-2, mod) % mod)) % mod
 return da