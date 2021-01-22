import itertools as i
f=lambda:tuple(map(int,input().split()))
x=list(i.permutations(range(1,int(input())+1)))
print(abs(-~x.index(f())--~x.index(f())))