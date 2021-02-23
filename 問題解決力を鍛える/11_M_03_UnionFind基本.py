def find(x):
    if par[x] == x: # 親が自分自身の時はroot
        return x
    else:
        # 経路圧縮なし
        #return find(par[x])

        #経路圧縮
        # xの親をrootにしておく
        par[x] = find(par[x]) 
        return par[x]

def same(x,y):
    return find(x) == find(y)


def unite(x,y):
    # 各グループのrootを見つける
    x = find(x) 
    y = find(y)
    
    # すでに同じグループの場合には何もしない
    if x == y: 
        return 0
    
    # 本来はsizeによって変えたい (Union by Size)
    par[x] = y
    