import heapq
p = list()
q = list()

def insert(x):
    heapq.heappush(p, x)
    return

def erase(x):
    heapq.heappush(q, x)
    return

def minimum():
    while q and p[0] == q[0]:
        heapq.heappop(p)
        heapq.heappop(q)
    return p[0]