i1=lambda : input()
i2=lambda : int(input())
i3=lambda : map(int,input().split())
i4=lambda : list(map(int,input().split()))
i5=lambda n : [list(map(int,input().split())) for _ in range(n)]
i6=lambda n : [list(input())for _ in range(n)]
 
 
N=i2()
S=i6(N)
T=i6(N)
 
 
# N=5
# S=[['.', '.', '.', '.', '.'], ['.', '.', '#', '.', '.'], ['.', '#', '#', '#', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]
# T=[['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '#'], ['.', '.', '.', '#', '#'], ['.', '.', '.', '.', '#']]
 
def scount(S):
    ans=0
    N=len(S)
    for i in range(N):
        ans+=S[i].count("#")
    return ans
 
def rtvCol(col,S):
    N=len(S)
    ans=[]
    for i in range(N):
        ans.append(S[i][col])
    return ans
 
def rotate(S):
    row=len(S)
    col=len(S[0])
    #print(row,col)
    #print("-"*10)
    ans=[]
    for i in range(col):
        t=[]
        for j in range(row-1,-1,-1):
            #print(j,i)
            t.append(S[j][i])
        ans.append(t)
    return ans
 
def checklist(S,T):
    l=len(S)
    ans=True
    for i in range(l):
        if ''.join(S[i])!=''.join(T[i]):
            return False
    return True
 
def pos(S):
    N=len(S)
    top=0
    for i in range(N):
        if "#" in S[i]:
            top=i
            break
 
    bottom=N
    for i in range(N-1,-1,-1):
        if "#" in S[i]:
            bottom=i
            break
 
    left=0
    for i in range(N):
        col=rtvCol(i,S)
        #print(col)
        if "#" in col:
            left=i
            break
 
    right=N
    for i in range(N-1,-1,-1):
        col=rtvCol(i,S)
        #print(i,col)
        if "#" in col:
            right=i
            break
        
    source=[]
    for i in range(top, bottom+1):
        t=[]
        for j in range(left,right+1):
            t.append(S[i][j])
        source.append(t)
    return ([top,bottom,left,right],source)
 
if scount(S)!=scount(T):
    ans=False
else:
    pos_s,source=pos(S)
    pos_t,target=pos(T)
    ans=False
    for i in range(4):
        t=checklist(source,target)
        if t:
            ans=True
            break
        target=rotate(target)
    
print('Yes' if ans else 'No')