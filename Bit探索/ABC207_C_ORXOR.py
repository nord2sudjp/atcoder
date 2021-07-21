N=int(input())
*A,=list(map(int,input().split()))


# N=3
# A=[1,5,7]

def main():
    ans=float('inf')

    for i in range(2**(N-1)): 
        t_ans=0
        c=0
        for j in range(N):
            c=c|A[j]
            if (i>>j&1):
                t_ans=t_ans^c
                c=0
            #c+=1 #A[j]
        t_ans=t_ans^c
        #print(t_ans)

        if t_ans<ans:
            ans=t_ans
    print(ans)
main()


N=int(input())
*A,=list(map(int,input().split()))


# N=3
# A=[1,5,7]

bit_len=N-1
ans=[]

for i in range(2**N): 
    t_ans=[]
    c=0
    for j in range(N):
        c=c|A[j]
        if (i>>j&1):
            t_ans.append(c)
            c=0
        #c+=1 #A[j]
    t_ans.append(c)
    #print(t_ans)
    
    x=0
    for a in t_ans:
       x ^= a 
    ans.append(x)
print(min(ans))