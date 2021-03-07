import sys

dic={}
for i in range(97, 97+26):
    dic[chr(i)]=0
#print(dic)

S=[]
for l in sys.stdin:
    S.append(l)
   
    
for s in S:
    for t in s:
    	if t.isalpha():dic[t.lower()]+=1

for k,v in dic.items():
    print(k+" : " + str(v))