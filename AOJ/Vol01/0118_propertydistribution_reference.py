dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
field = []
H, W = 0, 0
stack = []

def solver(x, y, symbol):
  global stack, field, H, W
  while True:
    if x < 0 or y < 0 or x >= H or y >= W:
      continue
    for dx, dy in dxy:
      if x+dx < 0 or y+dy < 0 or x+dx >= H or y+dy >= W:
        continue
      if field[x+dx][y+dy] == symbol:
        field[x+dx][y+dy] = '.'
        stack.append([x+dx, y+dy])
    if len(stack) == 0:
      return
    x, y = stack.pop()

while True:
  H, W = map(int, raw_input().split())
  if H == 0 and W == 0:
    break
  field = [list(raw_input()) for i in range(H)]

  ans = 0
  for x in xrange(H):
    for y in xrange(W):
      if field[x][y] != '.':
        solver(x, y, field[x][y])
        ans += 1
  print ans