# 
def f(S):
    l=len(S)
    b=[0]*l
    done=[0]*l
    i=0
    for i in range(l):
        if done[i]:continue # forはiを変更できない
        target=S[i]
        x=0
        while i+x<l:
            if S[i]!=S[i+x]:break
            x+=1
        print(i,S[i],x)
        for j in range(i,i+x):
            b[j]=x
            done[j]=1
    return ''.join(map(str,b))
f("aabbccccdddee")

# 番兵法
def f(S):
    S+='$'
    L=len(S)

    b=['']*(L-1)
    lake=S[0]
    s=0
    i=1
    while i<L: # forで回せば番兵は必要ない
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
