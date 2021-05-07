import sys

class Node:
    def __init__(self, next_node, prev_node, val):
        self.next = next_node
        self.prev = prev_node
        self.val = val

    def __repr__(self):
        return f'{self.val}'


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = self.head

    def append(self, val):
        node = Node(None, self.tail, val)
        self.tail.next = node
        self.tail = node

    def dump(self):
        cur = self.head.next
        out = ''
        while cur is not None:
            out += f'{cur.val} '
            cur = cur.next
        print(out[:-1])

    def splice(self, other):
        self.tail.next = other.head.next
        self.tail = other.tail

    def clear(self):
        self.__init__()