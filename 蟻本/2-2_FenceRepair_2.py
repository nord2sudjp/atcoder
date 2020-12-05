#N=3
#L=[8,5,8]

N=int(input())
*L,*=map(int,input().split())

a=0
i=0
while i<N-1:
  a+=L[i]+L[i+1]
  L[i+1]=a
  i+=1  
print(a)