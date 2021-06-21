# Volume3-0368 Flag

W,H,C=input().split()

W=int(W)
H=int(H)
# W=9
# H=5
# C='A'

ans=[]
for h in range(H):
        if h==0 or h==H-1:
            ans.append('+'+'-'*(W-2)+'+')
        elif h==H//2:
            ans.append('|'+'.'*((W-2)//2)+C+'.'*((W-2)//2)+'|')
        else:
            ans.append('|'+'.'*(W-2)+'|')
#print(ans)

for a in ans:
    print(''.join(a))
