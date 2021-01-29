N=int(input())
HS=[list(map(int,input().split())) for _ in range(N)]

rec=[]
for i in range(N):
    h,s=HS[i]
    rec.append([h+s*j for j in range(N)])

#print(rec)

rec_max=[i[-1] for i in rec]
#print(rec_max)

rec_dic=[]
for a in range(len(rec_max)):
    rec_dic.append((rec_max[a],a))
rec_dic_s=sorted(rec_dic, key=lambda x: x[0], reverse=True) 

#print(rec_dic_s)

ans=0
for i in range(N):
    s,t=rec_dic_s[i]
    #print(s,t,rec[t][i])
    ans=max(ans,rec[t][i])
print(ans)