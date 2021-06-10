while True:
    N=int(input())
    if N==0:break
        
    D=[0]*(N+1)
    D[0]=1

    for i in range(1,N+1):
     D[i]=(D[i-1]+D[i-2]+D[i-3])
    print( int(-((-D[-1]/10)//365))) 