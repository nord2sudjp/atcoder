# 0305 Yuekis' Audio Room

def isonline(R):
    return R%100==0

def isondegree(T):
    return T%30==0


# Q=[[300,120],[300,105],[250,105],[250,90]]

N=int(input())
Q=[list(map(int,input().split())) for _ in range(N)]

for r,t in Q:
    if isonline(r) and isondegree(t):
        s=t//30*5+1
        x=r/100-1
        print(int(s+x))
    elif isonline(r):
        s=t//30*5+1
        x=r/100-1
        print(int(x+s),int(x+s+5))
    elif isondegree(t):
        s=t//30*5+1
        x=r//100-1
        print(int(x+s),int(x+s+1))
    else:
        s=t//30*5+1
        x=r//100-1
        print(int(x+s),int(x+s+1),int(x+s+5),int(x+s+6))