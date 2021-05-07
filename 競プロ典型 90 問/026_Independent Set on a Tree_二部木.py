# 026 - Independent Set on a Tree
 
# G,v-ローカル変数
# sys.stdin.readlines()
# 1^np
# main()
# v[p]の比較をdfs呼び出し前に
# ans0/1をdfsでセット
 
import sys
sys.setrecursionlimit(1000000)
 
ans0=[[],[]]
 
 
def dfs(i,np,G,v):
    v[i] = np
    ans0[np].append(i)
    np=1^np
    for p in G[i]:
        if v[p]==-1 :dfs(p,np,G,v)
    return
 
def main():
    N=int(input())
    G = [[] for i in range(N+1)]
 
    for l in sys.stdin.readlines():
    #for i in range(N-1):
        a,b = map(int, l.split())
        G[a].append(b)
        G[b].append(a)
 
    # N=4
    # G=[[],[2],[3,4],[2],[2]]
    MAXN=N+1
 
    v=[-1]*(MAXN)
 
    dfs(1,1,G,v)
 
#     for i in range(1,MAXN):
#         if v[i]==0:
#             ans0.append(i)
#         else:
#             ans1.append(i)
 
    if len(ans0[0]) < len(ans0[1]):
        ans=ans0[1]
    else:
        ans=ans0[0]
    #print(ans0,ans1)
 
    print(' '.join(map(str,ans[:N//2])))
 
main()