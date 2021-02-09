import sys
sys.setrecursionlimit(10 ** 9)

N=int(input())
*S,=map(int,input().split())

ans=0
marks=[]

def solve(i,tans,mark):
    global ans
    if len(S)-1<=i:
        if tans==S[-1]: 
            ans+=1
            marks.append(mark)
        return
    tans_p=tans+S[i]
    tans_m=tans-S[i]
    i+=1
    if 0 <= tans_p <= 20:
        solve(i,tans_p,mark+"+")
    if 0 <= tans_m <= 20:
        solve(i,tans_m,mark+"-")

solve(0,0,'')
print(ans)
# print(marks)