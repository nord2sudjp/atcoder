N,M=map(int, input().split())
A=set(int(input()) for _ in range(M))
D=[0]*(N+1)
D[0]=1

for i in range(1,N+1):
 if i in A: continue
    # 飛ばす階段はそこまでの分岐が0とする。
 D[i]=(D[i-1]+D[i-2])%(10**9+7) # modの和算で対応
    # i-2, i-1がout of rangeの場合、右端の値となる。これは0なので影響がない
print(D[-1])