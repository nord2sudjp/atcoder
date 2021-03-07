# G は隣接リスト表現の形式で与えられます。各頂点には 1 から n までの番号がふられています。
# 各隣接リストの頂点は番号が小さい順に並べられています。
# プログラムは各頂点の発見時刻と完了時刻を報告します。
# 深さ優先探索の過程において、訪問する頂点の候補が複数ある場合は頂点番号が小さいものから選択します。
# 最初に訪問する頂点の開始時刻を 1 とします。


# N=4
# G=[[2],[4],[],[3]]
import sys
sys.setrecursionlimit(1000000)

N=int(input())
G=[list(map(int, input().split()))[2:] for _ in range(N)]

v=[False]*N
d=[0]*N
f=[0]*N
timecount=1

def dfs(i):
    global timecount
    if v[i] : return
    v[i] = True
    d[i] = timecount
    # print("D",i+1,timecount)
    timecount += 1
    for p in G[i]:
        dfs(p-1)
    # print("F",i+1,timecount)
    f[i] = timecount
    timecount += 1
    return

for i in range(N):
  if v[i]==0: dfs(i)

for i in range(N):
    print(i+1, d[i], f[i])