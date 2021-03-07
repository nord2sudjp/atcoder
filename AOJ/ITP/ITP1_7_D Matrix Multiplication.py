def get_inner_prod(raw, col):
    return sum([x*y for (x,y) in zip(raw,col)])

def get_matrix_trans(matrix):
    # malloc n*m matrix
    matrix_t = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix_t[j][i] = matrix[i][j]

    return matrix_t

def get_matrix_mul(matrix1, matrix2):
    # malloc A_m*B_n matrix
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    matrix2_t = get_matrix_trans(matrix2)
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = get_inner_prod(matrix1[i], matrix2_t[j])

    return result


N,M,L=map(int,input().split())

f=lambda:list(map(int,input().split()))

matrix1=[f() for _ in range(N)]
matrix2=[f() for _ in range(M)]

mat=get_matrix_mul(matrix1,matrix2)
for s in mat:
    print(' '.join(map(str,s)))