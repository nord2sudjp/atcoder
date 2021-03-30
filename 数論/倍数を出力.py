#
N=5
for i in range(N+N,31,N):
    print(i)

#
N=5
i=N+N
while i<31:
    print(i)
    i+=N

#
N=5
t=2
i=t*N
while i<31:
    print(i)
    t+=1
    i=t*N

#
N=10
for i in range(N,0,-1):
    for j in range(i+i,N+1,i):
        print(i,j)
        
        
#
N=10
a=[0]+list(range(1,N+1))
for i in range(N,0,-1):
    print(a[i+i::i])