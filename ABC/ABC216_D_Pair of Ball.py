# Yes��No�̏ꍇ�����_���ł������͐�������

i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]

from heapq import heappop, heappush
from collections import deque

def main():
    N,M=i3()

    A=[[]]
    q=[]
    mem=[[] for _ in range(N+1)]
    for i in range(M):
        k=i2()
        *t,=i4()
        t=t[::-1] # �t�]������
        A.append(t)
        mem[t[-1]].append(i+1) # �t�]���������疖�����擪

#     N,M=2,2
#     A=[[], [2, 1], [2, 1]]
#     # ����A��T������͎��Ԃ������遨�{�[��i���ǂ��ɂ���̂��������Ƀ������Ă����΂悢
#     mem=[[], [1, 2], []]
    
    q=deque()
    for i in range(1,N+1):
        if len(mem[i])==2:
            q.append(i)
    
    while q:
        v = q.pop() # v:pipes
        for p in mem[v]: #p:pipes
            A[p].pop()
            if len(A[p])!=0:
                mem[A[p][-1]].append(p)
                if len(mem[A[p][-1]])==2:
                    q.append(A[p][-1])

    for p in A:
        if len(p)!=0:
            print('No')
            return
    print('Yes')
    
main()