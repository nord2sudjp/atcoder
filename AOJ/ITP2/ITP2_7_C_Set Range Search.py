# ITP2_7_C
# TLE

from sys import stdin
import bisect

def bisect_slice(A,L,R):
    if len(A)==0:return []
    if R<L: return []
    index_l=bisect.bisect_left(A,L)
    index_r=bisect.bisect_left(A,R)
    if index_r<len(A) and A[index_r]==R:
        index_r+=1
    return A[index_l:index_r]

S=[]

n = stdin.readline()
queries = stdin.readlines()
#count = 0
for query in queries:
    query = query.split()
    if query[0] == '0':
        target=int(query[1])
        index=bisect.bisect_left(S,target)
        #print(len(S),index)
        if len(S)==index or S[index]!=target:
            S.insert(index,target)
        print(len(S))
    elif query[0] == '1':
        target=int(query[1])
        index=bisect.bisect_left(S,target)
        if index<len(S) and S[index]==target:
            print(1)
        else:
            print(0)
    elif query[0] == '2':
        target=int(query[1])
        index=bisect.bisect_left(S,target)
        if index<len(S) and S[index]==target:
            S.pop(index)
    else:
        L=int(query[1])
        R=int(query[2])
        x=bisect_slice(S,L,R)
        for _ in x:
          print(_)
        #print(' '.join(map(str,t)))