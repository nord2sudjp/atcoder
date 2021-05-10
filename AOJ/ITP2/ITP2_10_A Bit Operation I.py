# ITP2_10_A

N=int(input())


print(format(N, '032b'))
print(format(~N & 0b11111111111111111111111111111111,'032b'))

s=format(N<<1, '032b')
l=max(0,len(s)-32)
print(s[l:])
print(format(N>>1, '032b'))
