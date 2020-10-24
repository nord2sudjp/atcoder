S=input()
T=input()

a=False
ti=si=0
while ti<len(T):
    a=False
    while si<len(S):
        print(T[ti],S[si])
        if S[si]==T[ti]:
            a=True
            si+=1
            break
        si+=1
    else:
        break
    ti+=1
print(a)