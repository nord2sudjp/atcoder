S=input()
T=input()

a=False
for i in range(len(S)):
    if S[i]==T:
        a=True
        break
print(a)
