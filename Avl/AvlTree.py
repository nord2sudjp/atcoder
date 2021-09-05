class Avltree:
    """
    AVL��
 
    Methods
    -------
        search(x: int) -> Union(int)
            ��.data == x �̂��̂����݂��邠��ꍇ������o�́A�Ȃ��ꍇ None ��Ԃ�
        insert(x: int) -> None
            ��.data == x ���Ȃ��ꍇ ��.data == x �Ȃ钸�_�����B����ꍇ�͂Ȃɂ����Ȃ��i�㏑�����Ȃ��j
        y.to_s() -> int
            ���_y��data��Ԃ�
        y.left_s() -> Union(int, key=None)
            ���_y��left��Ԃ�(�Ȃ��ꍇ�� key)
        search_lower(x: int, key_lower) -> int
            ��.data �� x ��菬�������̂̒��ōł��傫�����̂��o�́A�Ȃ��ꍇ key_lower ��Ԃ�
        search_higher(x:int , key_higher) -> int
            ��.data �� x ���傫�����̂̒��ōł����������̂��o�́A�Ȃ��ꍇ key_higher ��Ԃ�
    """
 
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.balance = "Even"
 
    def search(self, key):
        node = self
        while node is not None:
            if node.key == key:
                return node  # node.key == key�̏ꍇ
            if node.key > key:
                node = node.left
            elif node.key < key:
                node = node.right
        return None
 
    def search_lower(self, key, key_lower):
        node = self
        if node.key is None:
            return key_lower
        ans = key_lower
        while node is not None:
            if node.key < key:
                if ans < node.key:
                    ans = node.key
                node = node.right
            elif node.key >= key:
                node = node.left
        return ans
 
    def search_higher(self, key, key_higher):
        node = self
        if node.key is None:
            return key_higher
        ans = key_higher
        while node is not None:
            if node.key > key:
                if ans > node.key:
                    ans = node.key
                node = node.left
            elif node.key <= key:
                node = node.right
        return ans
 
 
    def end_lower(self, end_lower_key):
        node = self
        while node.left is not None:
            node = node.left
        return node.key
 
    def end_higher(self, end_higher_key):
        node = self
        while node.right is not None:
            node = node.right
        return node.key
 
 
    def DoubleRightRotation(self):
        tl = self.left
        self.left = tl.right.right
        tl.right.right = self  # self�͂��̃m�[�h
        tlr = tl.right
        tl.right = tlr.left
        tlr.left = tl
        if tlr.balance == "Left":
            tlr.right.balance = "Right"
            tlr.left.balance = "Even"
        elif tlr.balance == "Right":
            tlr.right.balance = "Even"
            tlr.left.balance = "Left"
        elif tlr.balance == "Even":
            tlr.right.balance = "Even"
            tlr.left.balance = "Even"
        tlr.balance = "Even"
        return tlr
    def DoubleLeftRotation(self):
        tr = self.right
        self.right = tr.left.left
        tr.left.left = self
        trl = tr.left
        tr.left = trl.right
        trl.right = tr
        if trl.balance == "Right":
            trl.left.balance = "Left"
            trl.right.balance = "Even"
        elif trl.balance == "Left":
            trl.left.balance = "Even"
            trl.right.balance = "Right"
        elif trl.balance == "Even":
            trl.left.balance = "Even"
            trl.right.balance = "Even"
        trl.balance = "Even"
        return trl
    def SingleLeftRotation(self):
        tr = self.right
        tr.balance = "Even"
        self.balance = "Even"
        self.right = tr.left
        tr.left = self
        return tr
    def SingleRightRotation(self):
        tl = self.left
        tl.balance = "Even"
        self.balance = "Even"
        self.left = tl.right
        tl.right = self
        return tl
    def replace(self, p, v):  # �e�m�[�hp�̉��ɂ��鎩��(self)��v�ɒu��������B
        if p.left == self:
            p.left = v
        else:
            p.right = v
    def insert(self, key):  # root�ł̂݌Ă΂��}��
        if self.key is None:  # root���܂�rotation�͂��Ȃ����Ƃɂ���B
            self.key = key
            return self
        if key < self.key:
            if self.left is None:
                self.left = Avltree(key)
            else:
                self.left.insertx(self, key)
        elif key > self.key:
            if self.right is None:
                self.right = Avltree(key)
            else:
                self.right.insertx(self, key)
        else:  # key == self.key:
            pass  # do not overwrite
    def insertx(self, p, key):  # replace���ĂԂ��߂Ɉ��̐e�������Ă���insert
        node = self
        s = []
        while True:
            if node.key > key:
                s.append((node, -1))
                if node.left is None:
                    node.left = Avltree(key)
                    node = node.left
                    break
                else:
                    node = node.left
            elif node.key < key:
                s.append((node, 1))
                if node.right is None:
                    node.right = Avltree(key)
                    node = node.right
                    break
                else:
                    node = node.right
        while len(s) != 0:
            node, direct = s.pop()
            if len(s) != 0:
                par = s[-1][0]
            else:
                par = p
            if direct == -1:
                if node.balance == "Right":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Left"
                elif node.balance == "Left":
                    if node.left.balance == "Right":
                        node.replace(par, node.DoubleRightRotation())
                    elif node.left.balance == "Left":
                        node.replace(par, node.SingleRightRotation())
                    break
            elif direct == 1:
                if node.balance == "Left":
                    node.balance = "Even"
                    break
                elif node.balance == "Even":
                    node.balance = "Right"
                elif node.balance == "Right":
                    if node.right.balance == "Left":
                        node.replace(par, node.DoubleLeftRotation())
                    elif node.right.balance == "Right":
                        node.replace(par, node.SingleLeftRotation())
                    break
 
    def to_s(self):
        return self.key
    def left_s(self):
        if self.left is None:
            return None
        return (self.left).key
    def right_s(self):
        if self.right is None:
            return None
        return (self.right).key