# 0362 Trampoline

def main():
    N=int(input())
    T=[]
    for _ in range(N):
        T.append(int(input()))
#     N=4
#     T=[20,30,1,20]

#     N=10
#     T=[10, 29, 61, 1, 19, 21, 9, 1, 10, 40]

    maxd=0
    dis=0
    for i in range(N):
        dis=i*10
        if maxd<dis:
            print('no')
            return
        maxd=max(maxd,dis+T[i])

    T=T[::-1]

    maxd=0
    dis=0
    for i in range(N):
        dis=i*10
        if maxd<dis:
            print('no')
            return
        maxd=max(maxd,dis+T[i])

    print('yes')
    return
main()
