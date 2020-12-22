def f(S):
    S+='$'
    L=len(S)

    b=['']*(L-1)
    lake=S[0]
    s=0
    i=1
    while i<L: # for‚Å‰ñ‚¹‚Î”Ô•º‚Í•K—v‚È‚¢
        if S[i]=='$' or lake[0] != S[i]:
         l=len(lake)
         print(s,i,lake)
         for j in range(s,i):
            b[j]=str(l)
         s=i
         lake=S[i]
        else:
         lake+=S[i]
        i+=1
    return ''.join(b)
f("aabbccccdddee")

'2222444433322'
