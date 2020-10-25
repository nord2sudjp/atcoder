n = int(input())
s = input()
s1, s2, s3 = set(), set(), set()
for i in s:
    for j in s2:
        s3.add(j+i)
    for j in s1:
        s2.add(j+i)
    s1.add(i)
print(len(s3))