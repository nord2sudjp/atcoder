x="12"
v=0
wj=4
for c in x:
    print(c,v,v*wj,v*wj+int(c))
    v=v*wj+int(c)
print(v)