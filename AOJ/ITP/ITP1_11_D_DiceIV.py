# 11_D

def toNorth(D):
    D["T"],D["Bo"],D["F"],D["Ba"] = D["F"],D["Ba"],D["Bo"],D["T"]
    return D

def toEast(D):    
    D["T"],D["Bo"],D["L"],D["R"] = D["L"],D["R"],D["Bo"],D["T"]
    return D

def rotation(D):
    D["F"],D["R"],D["Ba"],D["L"] = D["L"],D["F"],D["R"],D["Ba"]
    return D

def getRight(D):
    return D["R"]

def isSame(D1,D2):
    return True if D1["T"]==D2["T"] and D1["Bo"]==D2["Bo"] and D1["F"]==D2["F"] and D1["Ba"]==D2["Ba"] and D1["L"]==D2["L"] and D1["R"]==D2["R"] else False

def moveandcheck(D1,D2):
    for _ in range(4):
        toNorth(D2)
        for _ in range(4):
            toEast(D2)
            for _ in range(4):
                rotation(D2)
                if isSame(D1,D2):
                    return True
    return False

# N=3
# A=[[1,2,3,4,5,6],[6,2,4,3,5,1],[6,5,4,3,2,1]]

N=int(input())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

D=[]
for i in range(N):
    D.append({})
    D[i]={"T":A[i][0], "Bo":A[i][5], "F":A[i][1], "Ba":A[i][4], "L":A[i][3], "R":A[i][2]}

isdiff=True
for j in range(1,N):
    ans=moveandcheck(D[0],D[j])
    if ans:
        print('No')
        exit()
print('Yes')    
