# 0663 Three Integers

import collections

*A,=map(int,input().split())

c=collections.Counter(A)
c=sorted(c.items(),key=lambda x: x[1], reverse=True)
print(c[0][0])