# 0409 Floor
x,y=map(int,input().split())
#x=8
#y=-14

if x==0 and y==0:
    print(1)
else:

    xmin=0
    xmax=0
    ymin=0
    ymax=0

    f1=0
    f2=1

    i=1
    #while True:
    for i in range(1,10**6):
        t=i%4
        f=f1+f2
        if t==1: # extend to left
            xmin=xmax+1
            xmax=xmin+f-1
            #ymin
            ymax=ymin+f-1
        elif t==2:
            xmin=xmax-f+1
            #xmax
            ymin=ymax+1
            ymax=ymin+f-1
        elif t==3:
            xmax=xmin-1
            xmin=xmax-f+1
            ymin=ymax-f+1
            #ymax
        else:
            #xmin
            xmax=xmin+f-1
            ymax=ymin-1
            ymin=ymax-f+1
        #print(t,xmin,xmax,ymin,ymax)
        if xmin<=x<=xmax and ymin<=y<=ymax:
            break
        f1,f2=f2,f

    print(i%3+1)

