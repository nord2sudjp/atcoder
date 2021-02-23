N,M=map(int,input().split())

D=[]
for _ in range(N-1):
    D.append(int(input()))
    
T=[]
for _ in range(M):
    T.append(int(input()))


m=[0]*(N)
for i in range(N-1):
   m[i+1]=m[i]+D[i]

#print(m)

loc=0
total=0
for i in range(M):
    #print(T[i],loc,loc+T[i],abs(m[loc]-m[loc+T[i]]))
    total+=abs(m[loc]-m[loc+T[i]])
    loc+=T[i]
mod=10**5
print(total%mod)