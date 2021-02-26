N = 4
G= [[ 0, 10, 15, 20 ], [ 10, 0, 35, 25 ],[ 15, 35, 0, 30 ],[ 20, 25, 30, 0 ]] 
answer=[]
def tsp(v, currPos, count, cost): 
  
    if (count == N and G[currPos][0]): 
        answer.append(cost + G[currPos][0]) 
        return

    for i in range(N): 
        if (v[i] == False and G[currPos][i]):
            # �ċA�ł��łɖK�ꂽ�Ƃ���͂����K��Ȃ�
            # G[P][i]==0�̏ꍇ�Ȃ����Ă��Ȃ�
              
            # Mark as visited 
            v[i] = True
            tsp(v, i, count + 1, cost + G[currPos][i]) 
              
            # Mark ith node as unvisited 
            v[i] = False


# Boolean array to check if a node has been visited or not 
v = [False for i in range(N)] 

# Mark 0th node as visited 
v[0] = True

# Find the minimum weight Hamiltonian Cycle 
tsp(v, 0, 1, 0) 
# v: visited flag
# currPos : ���݂̏ꏊ��0
# �ŏ���count : 1 (�J�E���g=N)�ɂȂ����������Ă���
# cost : �ŏ���cost=0

# ans is the minimum weight Hamiltonian Cycle 
print(min(answer)) 