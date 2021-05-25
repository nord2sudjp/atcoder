# CGL_3_A
# https://tjkendev.github.io/procon-library/python/geometry/polygon_area.html
def polygon_area(N, P):
    return abs(sum(P[i][0]*P[i-1][1] - P[i][1]*P[i-1][0] for i in range(N))) / 2.

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

print(polygon_area(N,P))