# AC

import array
import bisect
L, Q = map(int, input().split())
 
arr = array.array("i", [0, L])
 
for i in range(Q):
  c, x = map(int, input().split())
  if c == 1:
    bisect.insort(arr, x)
  else:
    a = bisect.bisect_left(arr, x)
    print(arr[a]-arr[a-1])
    
    
    
# TLE

import bisect
L, Q = map(int, input().split())
 
#arr = array.array("i", [0, L])
arr=[0, L]


for i in range(Q):
  c, x = map(int, input().split())
  if c == 1:
    bisect.insort(arr, x)
  else:
    a = bisect.bisect_left(arr, x)
    print(arr[a]-arr[a-1])
    