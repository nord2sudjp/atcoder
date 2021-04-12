import itertools

def main():
#     s1="send"
#     s2="more"
#     s3="money"

    s1=input()
    s2=input()
    s3=input()


    source=set(s1+s2+s3)
    js=''.join(source)
    if len(js)>10:
        print("UNSOLVABLE")
        return
    e={}
    for s,t in enumerate(source):
        #print(s,t)
        e[t]=s
    t1=[e[v] for v in s1]
    t2=[e[v] for v in s2]
    t3=[e[v] for v in s3]
    #print(t1,t2,t3)

    issolved=False
    per=itertools.permutations(range(10), len(source))
    for _per in per:
        if _per[t1[0]]==0 or _per[t2[0]]==0 or _per[t3[0]]==0:continue
        v=w=x=0
        for t in t1:
            v=v*10+_per[t]
        for t in t2:
            w=w*10+_per[t]
        for t in t3:
            x=x*10+_per[t]
        #print(v,w,x)

        if v+w==x:
            issolved=True
            break
    if issolved:
        print(v)
        print(w)
        print(x)
    else:
        print("UNSOLVABLE")
            
main()


# Original Version
import itertools
 
def main():
#     s1="send"
#     s2="more"
#     s3="money"
 
    s1=input()
    s2=input()
    s3=input()
 
    source=set(s1+s2+s3)
    js=''.join(source)
    if len(js)>10:
        print("UNSOLVABLE")
        return
 
    issolved=False
    for i in itertools.permutations(range(10), len(source)):
        dic={}
        for s,t in zip(source,i):
            #print(s,t)
            dic[s]=t
        #print(i)
        if dic[s1[0]]==0 or dic[s2[0]]==0 or dic[s3[0]]==0:continue
        v=w=x=0
        for t in s1:
            v=v*10+dic[t]
        for t in s2:
            w=w*10+dic[t]
        for t in s3:
            x=x*10++dic[t]
        if v+w==x:
            issolved=True
            break
 
    if issolved:
        print(v)
        print(w)
        print(x)
    else:
        print("UNSOLVABLE")
main()