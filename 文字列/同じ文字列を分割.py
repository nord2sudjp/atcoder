 S=input()+'$'
 L=len(S)
 
 lake=S[0]
 i=1
 while i<L:
   if S[i]=='$':
     print(lake)
   elif lake[0] != S[i]:
     print(lake)
     lake=S[i]
   else:
     lake+=S[i]
   i+=1