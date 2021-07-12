# 064 - Upliftiš3j

f=lambda : list(map(int,input().split()))

N,Q=map(int,input().split())
*A,=f()
U=[f() for _ in range(Q)]

# N=3
# Q=3
# A=[1, 2, 3]
# U=[[2, 3, 1], [1, 2, -1], [1, 3, 2]]


# N=20
# Q=10

# A=[61, 51, 92, -100, -89, -65, -89, -64, -74, 7, 87, -2, 51, -39, -50, 63, -23, 36, 74, 37]
# U=[[2, 2, -45], [6, 19, 82], [2, 9, 36], [7, 13, 71], [16, 20, 90], [18, 20, -24], [14, 17, -78], [10, 11, -55], [7, 19, -26], [20, 20, -7]]


E=0
for i in range(N-1):
    E += abs(A[i+1]-A[i])

D=[0]
for i in range(N-1):
    D.append(A[i+1]-A[i])


# print(E)


# print(D)
# print('-'*10)
for l,r,u in U:
    if l>1:
        if 0==D[l-1]:
            E+=abs(u)
        elif 0<D[l-1]: # increase
            if u>=0:
                E+=u
            else:
                a_l=abs(D[l-1])
                a_u=abs(u)
                if a_l>=a_u:
                    E-=a_u
                else:
                    E-=a_l
                    E+=(a_u-a_l)
        else:         # decrease
            if u<=0:
                E-=u
            else:
                a_u=abs(u)
                a_l=abs(D[l-1])
                if a_l>=a_u:
                    E-=a_u
                else:
                    E-=a_l
                    E+=(a_u-a_l)
        pl=D[l-1]
        D[l-1]+=u

    if r<N:

        if 0==D[r]:
            E+=abs(u)
        elif 0<D[r]:
            if u<=0:
                E-=u
            else:
                u=abs(u)
                pr=abs(D[r])
                if pr>=u:
                    E-=u
                else:
                    E-=pr
                    E+=(u-pr)
        else:
            if u>=0:
                E+=u
            else:
                a_u=abs(u)
                pr=abs(D[r])
                if pr>=a_u:
                    E-=a_u
                else:
                    E-=pr
                    E+=(a_u-pr)
        pr=D[r]
        D[r]-=u
    print(E)
    #print((l,r,u),E,pl,"=>",D[l-1] if l>1 else 0 , pr,"=>",D[r] if r<N else 0 )