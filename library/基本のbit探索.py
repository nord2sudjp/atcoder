
# デバッグバージョン
for i in range(2**n): 
    t=[]
    for j in range(n): 
        if (i>>j&1):
            t.append(j)
    print(i,'{:05b}'.format(i),' '.join(map(str,t))) # 出力