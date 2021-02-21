i1=lambda : input()
i2=lambda : int(input())

X=i1()
M=i2()
Xi=int(X)

mv=0

if len(X)==1:
    if Xi<=M:
        print(1)
    else:
        print(0)
    exit()

for x in X:
    mv=max(mv,int(x))
    
    
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
    
    
ac=mv
wa=M+1

while wa-ac>1:
  wj = (ac+wa)//2
  if bc(Xi,wj,10)<=M: # bc(Xi,wj,10)<=M‚È‚ç‚ÎðŒ‚ðŒ©‚½‚¢‚µ‚Ä‚¢‚é‚Ì‚Åac‚Å‚ ‚éB 
    ac = wj
  else:
    wa = wj

print(ac-mv)