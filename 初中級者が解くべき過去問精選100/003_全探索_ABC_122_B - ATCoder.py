S = input()
code = ["A", "T", "G", "C"]
w_count = 0
count = 0
for i in range(0,len(S)):
    if S[i] in code:
        w_count = w_count + 1
    else:
        if (count <= w_count): count = w_count
        w_count = 0
 
if (count <= w_count): count = w_count
print(count)