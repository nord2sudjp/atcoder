# https://tsutaj.hatenablog.com/entry/2017/03/29/204841


INF=10**16+1
INI=2**31-1

class Seg:
    # values = ソース数列
    # node_base = 最下段のノード数 (ソース数列の長さ以上になる最小の2**i)
    
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
        # qlow, ghigh -> query range, childrenでも値は変わらない
        # low, high -> segment range, 初期値は 0-N-1
        # pos = root of binary tree
        
        # partial overlap -> look at both child
        # total overlap -> tree rangeがquery rangeに含まれている -> treeの結果をそのまま返す
        # no overlap -> 重なっていない -> 適当な値を返す

        if (high < 0) : high = self.node_base;

        # 要求区間と対象区間が交わらない -> 適当に返す
        if(high <= qlow or qhigh <= low) : return INI;
        
        # total overlap 要求区間が対象区間を完全に被覆 -> 対象区間を答えの計算に使う
        if(qlow <= low and high <= qhigh) : return self.node[pos];
            

        #要求区間が対象区間の一部を被覆 -> 子について探索を行う
        #左側の子を vl ・ 右側の子を vr としている
        #新しい対象区間は、現在の対象区間を半分に割ったもの
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
