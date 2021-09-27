# https://tsutaj.hatenablog.com/entry/2017/03/29/204841


INF=10**16+1
INI=2**31-1

class Seg:
    # values = �\�[�X����
    # node_base = �ŉ��i�̃m�[�h�� (�\�[�X����̒����ȏ�ɂȂ�ŏ���2**i)
    
    def __init__(self,V):
        self.values=V
        data_size=len(V)
        self.node_base=1
        while (self.node_base < data_size):
            self.node_base*=2
        self.node=[INF]*(2*self.node_base-1)

        for i in range(data_size):
            self.node[i+self.node_base-1] = V[i];

        for i in range(self.node_base-2,-1,-1):
            self.node[i] = min(self.node[2*i+1], self.node[2*i+2]);

    def getNode(self):
        return self.node
            
    def update(self,x,val):
        x+=self.node_base-1
        self.node[x]=val
        while x>0:
            x=(x-1)//2
            self.node[x]=min(self.node[2*x+1],self.node[2*x+2])

    def getmin(self, qlow, qhigh, low=0, high=-1, pos=0):
        # qlow, ghigh -> query range, children�ł��l�͕ς��Ȃ�
        # low, high -> segment range, �����l�� 0-N-1
        # pos = root of binary tree
        
        # partial overlap -> look at both child
        # total overlap -> tree range��query range�Ɋ܂܂�Ă��� -> tree�̌��ʂ����̂܂ܕԂ�
        # no overlap -> �d�Ȃ��Ă��Ȃ� -> �K���Ȓl��Ԃ�

        if (high < 0) : high = self.node_base;

        # �v����ԂƑΏۋ�Ԃ������Ȃ� -> �K���ɕԂ�
        if(high <= qlow or qhigh <= low) : return INI;
        
        # total overlap �v����Ԃ��Ώۋ�Ԃ����S�ɔ핢 -> �Ώۋ�Ԃ𓚂��̌v�Z�Ɏg��
        if(qlow <= low and high <= qhigh) : return self.node[pos];
            

        #�v����Ԃ��Ώۋ�Ԃ̈ꕔ��핢 -> �q�ɂ��ĒT�����s��
        #�����̎q�� vl �E �E���̎q�� vr �Ƃ��Ă���
        #�V�����Ώۋ�Ԃ́A���݂̑Ώۋ�Ԃ𔼕��Ɋ���������
        mid = (low+high)/2
        vl = self.getmin(qlow, qhigh, low, mid, 2*pos+1);
        vr = self.getmin(qlow, qhigh, mid, high, 2*pos+2);
        return min(vl, vr);

    
N,Q=map(int,input().split())
OP=[list(map(int,input().split())) for _ in range(Q)]
# N,Q=1,3
# OP=[[1,0,0],[0,0,5],[1,0,0]]

V=[INI]*N    

seg=Seg(V)

for op,x,y in OP:
    if op==0: # update
        seg.update(x,y)
        #print(seg.getNode())
    else: # find
        print(seg.getmin(x,y+1))
