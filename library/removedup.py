from collections import deque
def removedup(x):
    d=deque()

    if len(x)==0:
        return ''
    d.append(x[0])

    l=len(x)
    for i in range(1,l):
        if len(d)==0:
            d.append(x[i])
        else:
            prv=d.pop()
            if x[i]!=prv:
                d.append(prv)
                d.append(x[i])
    return ''.join(list(d))

s='rehersaasreher'
print(removedup(s))

s='rehersaasrehe1'
print(removedup(s))