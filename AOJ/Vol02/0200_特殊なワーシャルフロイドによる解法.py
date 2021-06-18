def warshall_floyd(v_count: int, matrix: list) -> list:
    """ ワーシャルフロイド
    :param v_count: 頂点数
    :param matrix: 隣接行列(到達不能はfloat("inf"))
    """
    # 到達不能をfloat("inf")にしておけば余計なチェックを入れなくても
    # inf > inf+(-1) のような到達不能＋負辺が繋がってしまうことはない
    for i in range(v_count):
        for j, c2 in enumerate(row[i] for row in matrix):
            for k, (c1, c3) in enumerate(zip(matrix[j], matrix[i])):
                if c1 > c2+c3:
                    matrix[j][k] = c2+c3
    return matrix

while True:
    e_count, v_count = map(int, input().split())
    if not e_count:
        break
    inf = float("inf")
    edges_cost, edges_time = [[inf]*v_count for _ in [0]*v_count], [[inf]*v_count for _ in [0]*v_count]
    for _ in [0]*e_count:
        a, b, cost, time = map(int, input().split())
        a, b = a-1, b-1
        edges_cost[a][b] = cost
        edges_cost[b][a] = cost
        edges_time[a][b] = time
        edges_time[b][a] = time

    warshall_floyd(v_count, edges_cost)
    warshall_floyd(v_count, edges_time)

    for _ in [0]*int(input()):
        p, q, r = map(int, input().split())
        print((edges_time if r else edges_cost)[p-1][q-1])