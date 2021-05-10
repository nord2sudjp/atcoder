from sys import stdin
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=3714136


class LinkedList():
    def __init__(self):
        self.head = [None, None, None]
        self.head[1] = self.pos = self.tail = [self.head, None, None]
        # prev, next, value
        

    def insert(self, x):
        #temp = [self.pos[0], self.pos, x]
        # temp‚ðprevoius‚Ænext‚ÌŠÔ‚Éì‚é
        self.pos[0][1] = self.pos[0] = self.pos = [self.pos[0], self.pos, x]
        # prevous.next, current.previous, current‚ðtemp‚ÅXV

    def move_right(self, d):
        for _ in range(d):
            self.pos = self.pos[1]
            # current.next‚ðcurrent

    def move_left(self, d):
        for _ in range(d):
            self.pos = self.pos[0]
            # current.previous‚ðcurrent

    def move(self, d):
        if d > 0:
            self.move_right(d)
        else:
            self.move_left(d * -1)

    def erase(self):
        self.pos[1][0] = self.pos[0]
        # current.next.prevous = current.previoius
        self.pos = self.pos[0][1] = self.pos[1]

    def to_list(self):
        index = self.head[1]
        out = []
        while(index[1] is not None):
            out.append(index[2])
            index = index[1]
        return out

n = stdin.readline()
queries = stdin.readlines()
ll = LinkedList()
#count = 0
for query in queries:
    #print(count)
    #count += 1
    query = query.split()
    if query[0] == '0':
        ll.insert(query[1])
    elif query[0] == '1':
        ll.move(int(query[1]))
    else:
        ll.erase()

print('\n'.join(ll.to_list()))
