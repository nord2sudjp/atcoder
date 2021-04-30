# 1_14_A Naive String Search
base = 37; mod = 10**9 + 9
pw = None
def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + ord(s[i])) % mod
    return h
# RH前に、必要な長さの最大値分のpow-tableを計算しておく

def setup_pw(l):
    global pw
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod

def get(h, l, r):
    return (h[r] - h[l] * pw[r-l]) % mod

# s="aabaaa"
# p="aa"

s=input()
p=input()

ht=rolling_hash(s)
hp=rolling_hash(p)

l=len(p)
setup_pw(l)
pattern=get(hp,0,l)

for i in range(len(s)-len(p)+1):
    if get(ht,i,i+l)==pattern:
        print(i)
