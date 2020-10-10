def _gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def _lcm(x,y):
    d = gcd(x, y);
    return x / d * y;

import math

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
    
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

for i in l:a*=i//gcd(a,i)

   
   