D=int(input())
N=int(input())
M=int(input())
shop=[int(input())for i in range(N-1)]
target=[int(input()) for i in range(M)]
 
shop=sorted([0,*shop,D])
def bs_d(key, target_list):
     low=0
     high=len(target_list)-1
     while 1 < high-low:
         mid = (low+high)//2
         t=target_list[mid] 
         # print('key:',key,'target:',t,'l&h:', low, '-', high, 'mid:', mid, dir(t,key))
         if t == key:
             return (mid,mid)
         elif key < t:
             high = mid
         else:
             low = mid
     else:
         return (low,high)
 
ans=0