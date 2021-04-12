import itertools

# s1="send"
# s2="more"
# s3="money"

s1=input()
s2=input()
s3=input()

source=set(s1+s2+s3)
#print(source)

issolved=False
for i in itertools.permutations('0123456789', len(source)):
    #print(i)
    transtab = s1.maketrans(''.join(source), ''.join(i))
    #print(transtab)
    x1=s1.translate(transtab)
    x2=s2.translate(transtab)
    x3=s3.translate(transtab)
    if x1[0]=='0' or x2[0]=='0':continue
    #print(x1,x2,x3)
    i1=int(x1)
    i2=int(x2)
    i3=int(x3)
    if i1==0 or i2==0:continue
    if i1+i2==i3:
        issolved=True
        break

if issolved:
    print(i1)
    print(i2)
    print(i3)
else:
    print("UNSOLVABLE")