f=lambda:map(int,input().split())
N,M=f()
*A,=f()
A=sorted(A)
BC=[]
for _ in range(M):
    BC.append(tuple(f()))

#print(A)
BC=sorted(BC, key=lambda x: x[1])[::-1] 
i=0
for b,c in BC:
    while i<N and c<=A[i]:
        i+=1
    if N<=i: break
    #print(i)
    for j in range(i,max(i+b,N)):
        A[j]=max(A[j],c)
    #print(A)
print(sum(A))