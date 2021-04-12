def strtoval(s):
    s=s[::-1]
    dec=1
    ans=0
    for x in s:
        ans+=int(x)*dec
        dec*=10
    return ans
strtoval("123")