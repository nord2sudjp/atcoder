import sys
sys.setrecursionlimit(10*18)


N,Q=map(int,input().split())

par=[i for i in range(N+1)]
size=[1]*N

def find(x):
    if par[x] == x: # �e���������g�̎���root
        return x
    else:
        # �o�H���k�Ȃ�
        #return find(par[x])

        #�o�H���k
        # x�̐e��root�ɂ��Ă���
        par[x] = find(par[x]) 
        return par[x]

def same(x,y):
    return find(x) == find(y)

def unite(x,y):
    # �e�O���[�v��root��������
    x = find(x) 
    y = find(y)
    
    # ���łɓ����O���[�v�̏ꍇ�ɂ͉������Ȃ�
    if x == y: 
        return 0
    
    sx = size[x] 
    sy = size[y]
    
    if sy < sx: # tree y���������̂ŁAy��x�ɋz��
        par[y] = x
        size[x] += sy
    else:
        par[x] = y  # tree x���������̂ŁAx��y�ɋz��
        size[y] += sx    

for _ in range(Q):
    c,x,y=map(int,input().split())
    if c==0: # unite
        unite(x,y)
    else:    # same
        print(1 if same(x,y) else 0)
        