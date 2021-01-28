# Python‚Å‚ÍTLE
# PyPy3‚ÅAC

import copy

def abs_count(G):
    G_t = [list(x) for x in zip(*G)]
    ans=[]
    for g in G_t:
        t=0
        for h in g:
            if h==0:
                t-=1
            else:
                t+=1
        ans.append(abs(t))
    return(ans)

RC=[]
R,C=map(int,input().split())

RC=[list(map(int,input().split())) for _ in range(R)]

#R=2
#C=5
#RC=[[0,1,0,1,0],[1,0,0,0,1]]

rc_new=[]
abs_table=[]
for i in range(2**R):
    t=[]
    #print(i,'{:05b}'.format(i))
    for j in range(R):
        if (i>>j&1):
            #print(i,'{:05b}'.format(i),str(j)+"Œ…–Ú‚ªON")
            t.append([1-i for i in RC[j]])
        else:
            t.append(RC[j])
    #print(i,t)
    x=abs_count(t)
    rc_new.append(x)
    abs_table.append(sum(x))
    
#print(abs_table)
#print(abs_table.index(max(abs_table)))
#print(rc_new[abs_table.index(max(abs_table))])

ans=0


for i in rc_new[abs_table.index(max(abs_table))]:
    ans+=(R+i)//2
print(ans)