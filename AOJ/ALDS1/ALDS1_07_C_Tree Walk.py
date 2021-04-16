# 7-C
from collections import deque

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

def preoder(n):
    children=[v for v in G[n][1] if v!=-1]
    q = deque()
    q.append(n)
    
    for c in children:
        q.extend(preoder(c))
    return q

def inorder(n):
    left, right=G[n][1]
    q = deque()
    
    if left != -1:
        q.extend(inorder(left))
    q.append(n)
    if right != -1:
        q.extend(inorder(right))
    return q


def outorder(n):

    left, right=G[n][1]
    q = deque()
    if left != -1:
        q.extend(outorder(left))
    if right != -1:
        q.extend(outorder(right))
    q.append(n)
    return q

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
# N=9
# G={0: [-1, [1, 4], [], 2, 0, 3], 1: [0, [2, 3], [4], 2, 1, 1], 4: [0, [5, 8], [1], 2, 1, 2], 2: [1, [-1, -1], [3], 0, 2, 0], 3: [1, [-1, -1], [2], 0, 2, 0], 5: [4, [6, 7], [8], 2, 2, 1], 8: [4, [-1, -1], [5], 0, 2, 0], 6: [5, [-1, -1], [7], 0, 3, 0], 7: [5, [-1, -1], [6], 0, 3, 0]}
root_node=-1
for i in range(N):
    t=G[i]
    if t[0]==-1:
        root_node=i
# print(root_node)
update_depth([root_node,-1],-1)
update_height(root_node)
l=preoder(root_node)
print("Preorder")
print(' '+' '.join(map(str, l)))

l=inorder(root_node)
print("Inorder")
print(' '+' '.join(map(str, l)))

l=outorder(root_node)
print("Postorder")
print(' '+' '.join(map(str, l)))