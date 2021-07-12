# 033 - Not Too Bright
#Test 1 1, 2 3, 3 3, 3 2, 10 10

def main(H,W):

    # H=2
    # W=3
    if H==1 or W==1:
        print(H*W)
        return
    v=[[0]*W for _ in range(H)]

    ans=0
    for h in range(0,H,2):
        for w in range(0,W,2):
            v[h][w]='#'
            ans+=1
            if h+1<H:v[h+1][w]='.'
            if w+1<W:v[h][w+1]='.'
            if h+1<H and w+1<W:v[h+1][w+1]='.'

#     for i in v:
#         print(''.join(i))
    print(ans)

    
H,W=map(int,input().split())
main(H,W)

# TEST_DATA=[[1,1],[2,3],[3,3],[3,2],[10,10],[11,11],[1,8]]
# for H,W in TEST_DATA:
#     main(H,W)