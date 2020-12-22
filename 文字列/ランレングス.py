# 

from itertools import groupby

def rle_list(S: str):
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
        
        
def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp+str(count)
            tmp = s[i]
            count = 1
    ans += tmp+str(count)
    return ans
    

# ƒ‰ƒ“ƒŒƒ“ƒOƒX‚Ì‰—p
def f(S,R):
    p=0
    l=len(R)
    b=[0]*len(S)
    for c in range(0,l,2):
        print(p,R[c+1],R[c])
        ri=int(R[c+1])
        if R[c] != '#':
            for i in range(p,p+ri):
                b[i]=ri
        p+=ri
    return b


def rle(s):
    tmp, count, ans = s[0], 1, ""
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            ans += tmp+str(count)
            tmp = s[i]
            count = 1
    ans += tmp+str(count)
    return f(s,ans)   


print(rle("###....##.."))
[0, 0, 0, 4, 4, 4, 4, 0, 0, 2, 2]
