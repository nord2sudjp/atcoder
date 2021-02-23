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
    
    # �{����size�ɂ���ĕς����� (Union by Size)
    par[x] = y
    