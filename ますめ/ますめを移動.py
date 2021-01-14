a=[1,1]
b=[4,2]

s=a[0]
e=b[0]+1
for i in range(s+1,e):
    print(a[0],a[1],i,a[1])
    a[0]=i

s=a[1]
e=b[1]+1
for i in range(s+1,e):
    print(a[0],a[1],a[0],i)
    a[1]=i
'''
1 1 2 1
2 1 3 1
3 1 4 1
4 1 4 2
'''