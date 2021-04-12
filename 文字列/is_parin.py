 def parin(S):
     l=len(S)
     if l==1: # 長さ1の時は値によらず回文である。
         return True
     if l%2==0:
         mark=l//2
         left=S[0:mark]
         right=S[mark:l]
         #print(left,right)
     else:
         mark=l//2
         left=S[0:mark]
         right=S[mark+1:l]
         #print(left,right)
     
     if left==right[::-1]: # reverseすること！！！
         return True
     else:
         return False