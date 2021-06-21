# Volume2-0221 FizzBuzz

import sys
from collections import deque


while True:
    M,N=map(int,input().split())
    if N==0 and M==0:break
        
    d=deque(list(range(1,M+1)))

    #S=sys.stdin.readlines()
    S=[input() for _ in range(N)]
    cnt=1
    for s in S:
        #s=input()
        p=d.popleft()
        #print(cnt,s,p,cnt%3,cnt%5,d)
        if cnt%3==0 and cnt%5==0:
            if s=="FizzBuzz":
                d.append(p)
        elif cnt%3==0:
            if s=="Fizz":
                d.append(p)
        elif cnt%5==0:
            if s=="Buzz":
                d.append(p)
        else:
            if int(s)==cnt: # ‚±‚ÌğŒ‚ª“ü‚Á‚Ä‚¢‚È‚©‚Á‚½
                d.append(p)
        if len(d)==1:break
        cnt+=1
    print(' '.join(map(str,sorted(list(d)))))
