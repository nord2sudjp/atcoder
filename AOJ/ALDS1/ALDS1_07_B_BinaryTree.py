# ALDS_1_7_B

def update_depth(nodes,depth):
    if nodes[0]==-1 and nodes[1]==-1:return
    depth+=1
    for n in nodes:
        if n==-1:continue
        t=G[n]
        t[4]=depth
        update_depth(t[1], depth)

def update_height(u):
    t=G[u]
    children=[v for v in t[1] if v!=-1]
    # print(children)
    h=[0]
    for c in children:
        h.append(update_height(c)+1)
    
    max_h=max(h)
    G[u][5]=max_h
    return max_h

N=int(input())
G={}
#G=[parents,[children], [sibling],degree,depth, height]
for _ in range(N):
    node, left, right=map(int,input().split())
    n=G.get(node,[-1,[],[],-1,-1,0])
    n[1]=[left,right]
    n[3]=len([v for v in n[1] if v!=-1])
    G[node]=n
    for c in n[1]:
        if c==-1:continue
        g=G.get(c, [-1,[],[],-1,-1,0])
        g[0]=node
        g[2]=[v for v in n[1] if v!=-1 and v!=c]
        G[c]=g
#print(G)

# N=9
# G={0: [-1, [1, 4], [], 2, -1, 0], 1: [0, [2, 3], [1, 4], 2, -1, 0], 4: [0, [5, 8], [1, 4], 2, -1, 0], 2: [1, [-1, -1], [2, 3], 0, -1, 0], 3: [1, [-1, -1], [2, 3], 0, -1, 0], 5: [4, [6, 7], [5, 8], 2, -1, 0], 8: [4, [-1, -1], [5, 8], 0, -1, 0], 6: [5, [-1, -1], [6, 7], 0, -1, 0], 7: [5, [-1, -1], [6, 7], 0, -1, 0]}

root_node=-1
for i in range(N):
    t=G[i]
    if t[0]==-1:
        root_node=i
# print(root_node)
update_depth([root_node,-1],-1)
update_height(root_node)
# print(G)

for i in range(N):
    t=G[i]
    ni="internal node"
    if t[0]==-1:
        ni="root"
    elif t[3]==0:
        ni="leaf"
    if len(t[2])==0:
      sc="-1"
    else:
      sc=''.join(map(str,t[2]))
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(i, t[0], sc, t[3], t[4], t[5], ni))
    # #G=[parents,[children], [sibling],degree,depth, height]
