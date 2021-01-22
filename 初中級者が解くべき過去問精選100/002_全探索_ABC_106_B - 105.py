N = int(input())
 
totalcount = 0
 
for j in range(1, N+1, 2):
    count = 0
    for i in range(1, N+1):
        if j % i == 0:
            count = count + 1
    if count == 8:
        totalcount = totalcount + 1
print(totalcount)