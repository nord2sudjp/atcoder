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