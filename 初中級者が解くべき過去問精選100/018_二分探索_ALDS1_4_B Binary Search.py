N=int(input())
*S,=map(int,input().split())
Q=int(input())
*T,=map(int,input().split())

# N=5
# S=[1,2,3,4,5]
# Q=3
# T=[9]

def bs(key, l):
    low=0
    high=len(l)-1 # �ő�l��index�̓��X�g�̒�������1������
    while low<=high: # low��high���Ⴂ����͏����𑱂���B
        mid = (low+high)//2
        if l[mid] == key:
            return True
        elif key < l[mid]: 
            high = mid-1 # ���̎��_��mid�ł͂Ȃ��̂�1���炷����
        else:
            low = mid+1  # ���̎��_��mid�ł͂Ȃ��̂�1���炷����
    else:
        return False
cnt=0
for i in T:
    if bs(i, S):
        cnt+=1
print(cnt)