N=int(input())
*S,=map(int,input().split())
Q=int(input())
*T,=map(int,input().split())

# N=5
# S=[1,2,3,4,5]
# Q=3
# T=[9]

def bs(key, l):
    low=0
    high=len(l)-1 # 最大値のindexはリストの長さから1を引く
    while low<=high: # lowがhighより低い限りは処理を続ける。
        mid = (low+high)//2
        if l[mid] == key:
            return True
        elif key < l[mid]: 
            high = mid-1 # この時点でmidではないので1つずらすこと
        else:
            low = mid+1  # この時点でmidではないので1つずらすこと
    else:
        return False
cnt=0
for i in T:
    if bs(i, S):
        cnt+=1
print(cnt)