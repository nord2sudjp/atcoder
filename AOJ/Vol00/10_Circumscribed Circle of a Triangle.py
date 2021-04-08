import math

def cc(points):
    a = points[0]
    b = points[1]
    c = points[2]
    d = points[3]
    e = points[4]
    f = points[5]

    aa = a * a
    bb = b * b
    cc = c * c
    dd = d * d
    ee = e * e
    ff = f * f

    py = ((e - a) * (aa + bb - cc - dd) - (c - a) * (aa + bb - ee- ff)) / (2 * (e - a)*(b - d) - 2 * (c - a) * (b - f))

    px = (2 * (b - f) * py - aa - bb + ee + ff) / (2 * (e - a)) \
        if (c == a) else (2 * (b - d) * py - aa - bb + cc + dd) / (2 * (c - a))

    r = math.hypot(px - a, py - b)

    print("%.3f %.3f %.3f" % (px, py, r))
    
n = int(input())

for i in range(n):
    points = list(map(float, input().split()))
    cc(points)