K=int(input())

D={'0':('0','1'), '9':('8','9')}
for i in range(1,9):
    D[str(i)]=(str(i-1),str(i),str(i+1))
L=[]


def dfs(s):
    if 10<len(s):return
    for d in D[s[-1]]:
        x=s+d
        L.append(x)
        dfs(x)

#dfs('1')
#L.append('1')

for i in range(1,10):
    L.append(str(i))
    dfs(str(i))
L=sorted(list(map(int, L)))
print(L[K-1])