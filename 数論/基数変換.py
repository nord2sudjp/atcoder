def bc(N, ibase, obase):
    t=list(str(N))
    nl=list(map(int,t))
    o = []
    while any(nl):
        c = 0
        for i in range(len(nl)):
            c = c * ibase + nl[i]
            nl[i],c = divmod(c,obase)
        o.append(c)
    o.reverse()
    
    return int(''.join(map(str,o)))
    