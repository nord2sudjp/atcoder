def euler_phi(n):
    res = n
    x = 2
    while x*x <= n: # x**2‚ªn‚æ‚è’á‚¢x‚É‚Â‚¢‚Ä
        if n % x == 0: # n‚ªx‚ÅŠ„‚èØ‚ê‚éê‡‚É‚ÍœŠO‚·‚é
            res = res // x * (x-1)
            while n % x == 0: # ‘fˆö”•ª‰ğ‚Åx‚É‚Â‚¢‚Äreduce‚µ‚Ä‚¢‚­ —á) 12=2**3*3‚Ì‚Æ‚«2**3‚ğÁ‚µ‚Ş
                n //= x
        x += 1
    if n > 1:
        res = res // n * (n-1)
    return res


print(euler_phi(int(input())))