# 300 Floppy cube

INF=float('inf')


def complete(p):
    finstate = [1,1,1,1,1,1,1,1,1,2,2,2,4,4,4,6,6,6,5,5,5,3,3,3,3,3,3,3,3,3]
    return p==finstate

    #t=any(p[1]!=p[i] for i in range(1,10))
    #if t:

    
#     for i in range(0,9):
#         if p[0]!=p[i]:
#                 return False
#     for i in range(21,30):
#         if p[21]!=p[i]:
#             return False
        
#     for i in range(9,12):
#         if p[9]!=p[i]:
#             return False
        
#     for i in range(12,15):
#         if p[12]!=p[i]:
#             return False

#     for i in range(15,18):
#         if p[15]!=p[i]:
#             return False
        
#     for i in range(18,21):
#         if p[18]!=p[i]:
#             return False
       
    #for i in range(9,21):
        #if i%3==1:s=p[i]
        #if p[i]!=p[(i-1)//3*3+1]:
        #if p[i]!=s:
        #    return False
#    return True

# replacement=[
#   [[1, 2, 3, 15, 19], [28, 29, 30, 16, 21]],
#   [[7, 8, 9, 13, 10], [22, 23, 24, 18, 12]],
#   [[1, 4, 7, 10, 16], [24, 27, 30, 21, 18]],
#   [[3, 6, 9, 12, 13], [22, 25, 28, 19, 15]]]

def k(comm,p):
    if comm==0:
        p[0],p[1],p[2], p[27],p[28],p[29] = p[27],p[28],p[29], p[0],p[1],p[2]
        p[14], p[15] = p[15], p[14]
        p[18], p[20] = p[20], p[18]
    elif comm==1:
        p[2],p[5],p[8], p[21],p[24],p[27] = p[21],p[24],p[27], p[2],p[5],p[8]
        p[11], p[18] = p[18], p[11]
        p[12], p[14] = p[14], p[12]
    elif comm==2:
        p[6],p[7],p[8], p[21],p[22],p[23] = p[21],p[22],p[23], p[6],p[7],p[8]
        p[12], p[17] = p[17], p[12]
        p[9], p[11] = p[11], p[9]
    elif comm==3:
        p[0],p[3],p[6], p[23],p[26],p[29] = p[23],p[26],p[29], p[0],p[3],p[6]
        p[9], p[20] = p[20], p[9]
        p[15], p[17] = p[17], p[15]
    return p
    
#     r=rep[0]
#     s=rep[1]
#     p[r[0]],p[r[1]],p[r[2]],p[r[3]],p[r[4]],p[s[0]],p[s[1]],p[s[2]],p[s[3]],p[s[4]] = p[s[0]],p[s[1]],p[s[2]],p[s[3]],p[s[4]],p[r[0]],p[r[1]],p[r[2]],p[r[3]],p[r[4]]
#     return p
    
#     for s,t in zip(rep[0],rep[1]):
#         #print(s,t)
#         p[s],p[t]=p[t],p[s]
#     return p


def dfs(count,p):
    if complete(p):return count
    if count>=8:return INF
    ans=INF
    for i in range(4):
        t=dfs(count+1,k(i,p))
        if ans>t:
            ans=t
        k(i,p)
    return ans
import sys

def main():
  N=int(input())
  I=sys.stdin.readlines()  
  for l in I:
      *p,=list(map(int,l.split()))
      #p=[0]+p
      ans=dfs(0,p)
      print(ans)

main()