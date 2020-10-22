def s(k):
    f=0
    if k%2==0 and k!=2:return False
    for d in range(2, k//2):
        if k%d == 0:return False
    return True
