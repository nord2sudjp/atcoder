”’lŒvŽZ‚æ‚è‚à•¶Žš—ñ‚ÌŒvŽZ‚ª‘‚¢

# B Multiple of 9 - TLE

N=int(input())

t=0

while N>0:
    t=t+N%10
    N=N//10
    
print('Yes' if t%9==0 else 'No')    


# B Multiple of 9 - AC

N=input()

t=0
for s in N:
    t=t+int(s)

print('Yes' if t%9==0 else 'No')    