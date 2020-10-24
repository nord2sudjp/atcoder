def f(S,T):
    a=False
    ti=si=0
    while ti<len(T):
        a=False
        while si<len(S):
            # print(T[ti],S[si])
            if S[si]==T[ti]:
                a=True
                si+=1
                break
            si+=1
        else:
            break
        ti+=1
    return(a)

N=int(input())
S=input()

a=0
for i in range(1000):
    s=str(i).zfill(3)
    if f(S,s):
        a+=1
        #print(S,s,'*')
    #else:
        #print(S,s)

print(a)