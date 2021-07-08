# 0619 Selecting Subjects

A=[int(input()) for _ in range(4)]
B=[int(input()) for _ in range(2)]

A.sort(reverse=True)
B.sort(reverse=True)

print(sum(A[:3])+sum(B[:1]))