N=int(input())
S=input()
import itertools
s=set(itertools.combinations(S, N-(N-3)))

print(len(s))