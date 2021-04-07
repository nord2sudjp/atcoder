#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1_A
print("Hello World")


# In[ ]:


# 1_B
N=int(input())
print(N**3)


# In[ ]:


# 1_C
N,M=map(int,input().split())
print(N*M, 2*N+2*M)


# In[ ]:


# 1_D
N=int(input())
h=N//3600
N%=3600
m=N//60
N%=60
print(str(h)+":"+str(m)+":"+str(N))


# In[ ]:


# 2_A
a,b=map(int,input().split())
if a<b:
    print("a < b")
elif a>b:
    print("a > b")
else:
    print("a == b")


# In[ ]:


# 2_B

a,b,c=map(int,input().split())

if a<b<c:
    print('Yes')
else:
    print("No")


# In[ ]:


# 2_C
*A,=map(int,input().split())

A=sorted(A)
print(' '.join(map(str,A)))


# In[ ]:


# 2_D
w,h,x,y,r=map(int,input().split())

max_x=x+r
min_x=x-r
max_y=y+r
min_y=y-r

if 0<=min_x and max_x<=w and 0<=min_y and max_y<=h:
    print('Yes')
else:
    print('No')


# In[ ]:


# 3_A
for _ in range(1000):
    print("Hello World")


# In[ ]:


# 3_B
i=1

while True:
    x=int(input())
    if x==0:break
    print('Case %d: %d' % (i,x))
    i+=1


# In[ ]:


# 3_C
while True:
    x,y=map(int,input().split())
    if x==y==0:break
    a=map(str,sorted([x,y]))
    print(' '.join(a))


# In[ ]:


# 3_D

a,b,c=map(int,input().split())

cnt=0
for i in range(a,b+1):
    if c%i==0:
        cnt+=1
print(cnt)


# In[ ]:


# 4_A
a,b=map(int,input().split())
from decimal import Decimal
# 2 100000009
print(a//b, a%b, "{0:.10f}".format(Decimal(a/b)))


# In[ ]:


# 4_B
from math import pi

r=float(input())
print(r*r*pi, 2*r*pi)


# In[ ]:


# 4_C

while True:
    a,op, b=input().split()

    if op=='?':
        break
    print(int(eval(a+op+b)))
    


# In[ ]:


# 4_D

N=int(input())
*A,=map(int,input().split())
A=sorted(A)
print(A[0],A[-1],sum(A))


# In[ ]:


# 5_A
while True:
    H,W=map(int,input().split())
    if H==W==0:break
    [print("#"*W) for _ in range(H)]
    print("")


# In[ ]:


# 5_B

while True:
    H,W=map(int,input().split())
    if H==W==0:break
    
    print("#"*W)
    s="#"+'.'*(W-2)+"#"
    [print(s) for _ in range(H-2)]
    print("#"*W)

    print("")


# In[ ]:


# 5_C

while True:
    H,W=map(int,input().split())
    if H==W==0:break

    s0="#."*(W//2+1)
    s0=s0[0:W]
    
    s1=".#"*(W//2+1)
    s1=s1[0:W]
    
    for i in range(H):
        if i%2==0:
            print(s0)
        else:
            print(s1)
    print("")


# In[ ]:


# 5_D

N=int(input())
i=0

s=[]
while True:
    i+=1
    if N<i:break
    x=i
    if x%3==0:
        s.append(i)
        continue
    while x!=0:
        if x%10==3:
            s.append(i)
            break
        x//=10
print(' ' + ' '.join(map(str,s)))


# In[ ]:


# 6_A

N=int(input())
*A,=map(int,input().split())

print(' '.join(map(str,A[::-1])))


# In[ ]:


# 6_B
N=int(input())

type=["S","H","C","D"]

card={}

for t in type:
    card[t]=set()

for _ in range(N):
    t,n=input().split()
    n=int(n)
    card[t].add(n)

for t in type:
    for i in range(1,14):
        if not({i} <= card[t]):
            print(t+" "+str(i))


# In[ ]:


# 6_C

B=[]
for i in range(4):
    r=[[0]*10 for _ in range(3)]
    B.append(r)
#print(B)

N=int(input())

for _ in range(N):
    b,f,r,p=map(int,input().split())
    b-=1
    f-=1
    r-=1
    B[b][f][r]+=p

for i in range(4):
    for j in range(3):
        print(" " + ' '.join(map(str,B[i][j])))
    if i!=3:
        print("####################")


# In[ ]:


# 6_D

N,M=map(int,input().split())

MT1=[list(map(int,input().split())) for _ in range(N)]
MT2=[int(input()) for _ in range(M)]

for i in range(N):
    s=MT1[i]
    ans=0
    for x,y in zip(s,MT2):
        ans+=x*y
    print(ans)


# In[ ]:


# 7_A

while True:
    m,f,r=map(int,input().split())
    
    if m==f==r==-1:
        break
    
    if m==-1 or f==-1:
        print("F")
    elif 80<=m+f:
        print("A")
    elif 65<=m+f:
        print("B")
    elif 50<=m+f:
        print("C")
    elif 30<=m+f:
        g="D"
        if 50<=r:
            g="C"
        print(g)
    else:
        print("F")


# In[ ]:


# 7_B How Many Ways?

l=[]
while True:
    n,x=map(int,input().split())
    if n==0 and x==0: break
    l.append((n,x))

for n,x in l:
    ans=0
    for h in range(1,n-1):
        for i in range(h+1,n):
            for k in range(i+1,n+1):
                if h+i+k==x: ans+=1
    print(ans)


# In[ ]:


# 7_C

r,c=map(int,input().split())

A=[list(map(int,input().split())) for _ in range(r)]

final=0
for i in range(r):
    s=A[i]
    t=sum(s)
    s.append(t)
    final+=t
    print(' '.join(map(str,s)))

total=[]

for i in range(c):
    t=0
    for j in range(r):
        t+=A[j][i]
    total.append(t)

total.append(final)
print(' '.join(map(str,total)))


# In[ ]:


# 7_D

def get_inner_prod(raw, col):
    print(raw,col)
    return sum([x*y for (x,y) in zip(raw,col)])

def get_matrix_trans(matrix):
    # malloc n*m matrix
    matrix_t = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t

def get_matrix_mul(matrix1, matrix2):
    # malloc A_m*B_n matrix
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    matrix2_t = get_matrix_trans(matrix2)
    print(matrix2_t)
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = get_inner_prod(matrix1[i], matrix2_t[j])

    return result


N,M,L=map(int,input().split())

f=lambda:list(map(int,input().split()))

matrix1=[f() for _ in range(N)]
matrix2=[f() for _ in range(M)]

mat=get_matrix_mul(matrix1,matrix2)
for s in mat:
    print(' '.join(map(str,s)))


# In[ ]:


# 8_A
S=input()

ans=''
for s in S:
    if s.islower():
        ans+=s.upper()
    else:
        ans+=s.lower()
print(ans)


# In[ ]:


# 8_B
while True:
    S=input()
    if S=='0':break
    ans=0
    for s in S:
        ans+=int(s)
    print(ans)


# In[ ]:


# 8_C

dic={}
for i in range(97, 97+26):
    dic[chr(i)]=0
#print(dic)

S=input()

for s in S:
    if s.isalpha():dic[s.lower()]+=1

for k,v in dic.items():
    print(k+" : " + str(v))


# In[ ]:


# 8_D
S=input()
T=input()

S+=S

if T in S:
    print('Yes')
else:
    print('No')    


# In[ ]:


# 9_A
T=input()

S=[]
while True:
    t=input()
    if t=="END_OF_TEXT":break
    S.extend(t.split())

A=[1 for s in S if s==T]
print(sum(A))


# In[ ]:


# 9_B


while True:
    s=input()
    if s=="-":break
    m=int(input())
    A=[int(input()) for _ in range(m)]
    
    for a in A:
        h=s[:a]
        s=s[a:]+h
        #print(h,s)
    print(s)


# In[ ]:


# 9_C
N=int(input())
S=[list(input().split()) for _ in range(N)]

#N=3
#S=[["cat", "dog"],["fish", "fish"],["lion", "tiger"]]

s_t=0
s_h=0

for t,h in S:
    #print(t,h)
    if t==h:
        s_t+=1
        s_h+=1
    elif t<h:
        s_h+=3
    else:
        s_t+=3
print(s_t,s_h)
        


# In[ ]:


# 9_D

S=input()
N=int(input())

for _ in range(N):
    s,*c=input().split()
    if s=="replace":
        l,r,t=c
        l=int(l)
        r=int(r)
        S=S[:l]+t+S[r+1:]
        #print(S)
    else:
        l,r=map(int,c)
        if s=="reverse":
            x=S[l:r+1]
            x=x[::-1]
            S=S[:l]+x+S[r+1:]
        else:
            print(S[l:r+1])


# In[ ]:


# 10_A
x1,y1,x2,y2=map(int,input().split())
print(((x1-x2)**2+(y1-y2)**2)**0.5)


# In[ ]:


# 10_B

import math

a,b,C=map(int,input().split())

S=0.5*a*b*math.sin(math.radians(C))
print(S)
print((a**2+b**2-2*a*b*math.cos(math.radians(C)))**0.5+a+b)
print(2*S/a)


# In[ ]:


# 10_C
import statistics
while True:
    N=int(input())
    if N==0:break
    S=list(map(int,input().split()))
    
    print(statistics.pstdev(S))


# In[ ]:


# 10_D
N=int(input())
*x,=map(int,input().split())
*y,=map(int,input().split())

dis_1=dis_2=dis_3=dis_f=0
dis_2
for s,t in zip(x,y):
    dis_1+=abs(s-t)
    dis_2+=(s-t)**2
    dis_3+=(abs(s-t))**3
    dis_f=max(dis_f,abs(s-t))
    
print(dis_1)
print((dis_2)**0.5)
print((dis_3)**(1/3))
print(dis_f)

dis=0
for s,t in zip(x,y):
    dis+=abs(s-t)


# In[ ]:


# 11_A
# https://eromog.hatenablog.com/entry/2015/05/29/000529
# https://tjkendev.github.io/procon-library/python/other/dice.html

# Top, Bottom, Front, Back, Left, Right
D={"T":1, "Bo":6, "F":2, "Ba":5, "L":4, "R":3}

*A,=list(map(int,input().split()))
S=input()

# A=[1,2,4,8,16,32]
# S="SE"

for d in S:
    if d=="N":
        D["T"],D["Bo"],D["F"],D["Ba"] = D["F"],D["Ba"],D["Bo"],D["T"]
    elif d=="S":
        D["T"],D["Bo"],D["F"],D["Ba"] = D["Ba"],D["F"],D["T"],D["Bo"]
    elif d=="E":
        D["T"],D["Bo"],D["L"],D["R"] = D["L"],D["R"],D["Bo"],D["T"]
    elif d=="W":
        D["T"],D["Bo"],D["L"],D["R"] = D["R"],D["L"],D["T"],D["Bo"]
    # print(d,"-",D["T"],D)
print(A[D["T"]-1])


# In[ ]:


# 11_B

def toNorth():
    D["T"],D["Bo"],D["F"],D["Ba"] = D["F"],D["Ba"],D["Bo"],D["T"]

def toEast():    
    D["T"],D["Bo"],D["L"],D["R"] = D["L"],D["R"],D["Bo"],D["T"]

def rotation():
    D["F"],D["R"],D["Ba"],D["L"] = D["L"],D["F"],D["R"],D["Ba"]

# A=[1,2,3,4,5,6]
# Q=[3,2]

*A,=list(map(int,input().split()))
N=int(input())
for _ in range(N):
    D={"T":A[0], "Bo":A[5], "F":A[1], "Ba":A[4], "L":A[3], "R":A[2]}

    p,q=map(int,input().split())

    for _ in range(3):
        if D['T']!=p:
            if p in [A[0],A[1],A[4],A[5]]:
                    toNorth()
            else:
                toEast()
    for _ in range(3):
        if D['F']!=q:
            rotation()

    print(D['R'])


# In[ ]:


# 11_B - WA

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


#A=[[1,2,3,4,5,6],[6,5,4,3,2,1]]

A=[]
A.append(list(map(int,input().split())))
A.append(list(map(int,input().split())))


for i in range(2):
    D[i]={"T":A[i][0], "Bo":A[i][5], "F":A[i][1], "Ba":A[i][4], "L":A[i][3], "R":A[i][2]}

for _ in range(3):
    p=D[0]['T']
    if D[1]['T']!=p:
        if p in [D[1]['T'],D[1]['Bo'],D[1]['F'],D[1]['Ba']]:
            D[1]=toNorth(D[1])
        else:
            toEast(D[1])
for _ in range(3):
    q=D[0]['F']
    if D[1]['F']!=q:
        rotation(D[1])

print('Yes' if getRight(D[0]) == getRight(D[1]) else 'No')


# In[ ]:


# 11_B - AC

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

#A=[[1,2,3,4,5,6],[6,5,4,3,2,1]]

A=[]
A.append(list(map(int,input().split())))
A.append(list(map(int,input().split())))

D=[]
for i in range(2):
    D.append({})
    D[i]={"T":A[i][0], "Bo":A[i][5], "F":A[i][1], "Ba":A[i][4], "L":A[i][3], "R":A[i][2]}

for _ in range(4):
    toNorth(D[1])
    for _ in range(4):
        toEast(D[1])
        for _ in range(4):
            rotation(D[1])
            if isSame(D[0],D[1]):
                print('Yes')
                exit()
print('No')


# In[ ]:


# 11_B - AC

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

#A=[[1,2,3,4,5,6],[6,5,4,3,2,1]]

A=[]
A.append(list(map(int,input().split())))
A.append(list(map(int,input().split())))

D=[]
for i in range(2):
    D.append({})
    D[i]={"T":A[i][0], "Bo":A[i][5], "F":A[i][1], "Ba":A[i][4], "L":A[i][3], "R":A[i][2]}

if moveandcheck(D[0],D[1]):
    print('Yes')
else:
    print('No')


# In[ ]:


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

