M=[[*map(int,input().split())] for i in [0]*int(input())]
 
c=10**11
for a,_ in M:
 for _,b in M:
  if b<a:continue
  c=min(c, sum(b-a+max((a-i)*2,0)+max((j-b)*2,0) for i,j in M))
print(c)