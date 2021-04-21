import sys

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def insert(key):
    global root
    
    if not(root): # root==Noneの場合には新しいノードを作るだけ
        root = Node(key)
        return
    
    ch=root
    while ch:
        pa=ch
        # keyによってleftとrightの移動先が決まる。
        # print(ch.key, key, "left" if key < ch.key else "right")
        if key < ch.key:
            ch=ch.left
        else:
            ch=ch.right
        # chがnullの場合には、ここでおしまい。
        
    # keyがpa.keyより小さくなったらNodeを作る
    # print(pa.key,key)
    if key < pa.key:
        pa.left = Node(key)
    else:
        pa.right = Node(key)

def find(key):
    ch=root
    while ch:
        if key == ch.key:return True
        if key < ch.key:
            ch=ch.left
        else:
            ch=ch.right
    return False

def delete(key)
    pa=None
    ch=root
    found=False
    direction=""
    while ch:
        if key == ch.key:
          found=True
          break
        pa=ch
        if key < ch.key:
            ch=ch.left
        else:
            ch=ch.right
    if not(found):return
    
    if pa.left == ch:
        if not(ch.right) and not(ch.left):
            pa.left=None
        elif not(ch.right):
            pa.left=ch.left
        elif not(ch.left):
            pa.left=ch.right
        else:
            
    else:
        if not(ch.right) and not(ch.left):
            pa.right=None
       
  
def walk(node, order, p):
  global walked
  if node:
    if order == "Pre":
        walked.append(node.key)
      #walked += f" {node.key}:{p}"
    walk(node.left, order, node.key)
    if order == "In":
        walked.append(node.key)
      #walked += f" {node.key}:{p}"
    walk(node.right, order, node.key)
  return   
            
root = None

N=int(input())
Nodes=set()

for l in sys.stdin.readlines():
    opr,*value=l.split()
    if opr=='insert':
      v1=int(value[0])
      insert(v1)
      Nodes.add(v1)
    elif opr=='find':
      v1=int(value[0])
      if find(v1):
        print('yes')
      else:
        print('no')
    elif opr=='print':
      walked=[]
      w=walk(root, "In", None)
      print(' ' + ' '.join(map(str,walked)))
      walked=[]
      w=walk(root, "Pre", None)
      print(' ' + ' '.join(map(str,walked)))
      