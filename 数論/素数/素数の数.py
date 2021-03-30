# https://szarny.hatenablog.com/entry/2017/09/21/232855#%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%89
def improve(limit):
    n = 0
    for k in range(2, limit+1):
        factor = 0
        
        # 2ˆÈŠO‚Ì‹ô”‚Í‘f”‚Å‚Í‚È‚¢‚Ì‚Å–³‹‚·‚é
        if k % 2 == 0 and k != 2:
            continue
        
        # ŒJ‚è•Ô‚µ‚ÌãŒÀ‚ğ”¼•ª‚É‚·‚é
        for divisor in range(2, k//2):
            if k % divisor == 0:
                factor += 1
                
        if factor == 0:
            n += 1
            
    return n
print(improve(int(input())))



# ã‹L‚Ìminimum version
def s(l):
    n=0
    for k in range(2,l+1):
        f=0
        if k%2==0 and k!=2:continue
        for d in range(2, k//2):
            if k%d == 0:
                f+=1
        if f==0:
            n+=1
    return n