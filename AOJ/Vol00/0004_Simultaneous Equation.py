import sys

for l in sys.stdin.readlines():
        a,b,c,d,e,f = map(int,l.split())
        x = (c * e - b * f) / (a * e - b * d)
        y = (a * f - c * d) / (a * e - b * d)
        x *= 1000
        x = x + (0.5 if x > 0 else -0.5)
        x = int(x)
        y *= 1000
        y = y + (0.5 if y > 0 else -0.5)
        y = int(y)
        print('{:.3f}'.format(x/1000),'{:.3f}'.format(y/1000))