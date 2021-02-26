def binary_search(A,T):
    left=0
    right=len(A)-1
    
    while right-left>1:
        mid = (left+right)//2
        #print(mid, left,right, a[mid])
        if T<=a[mid]:
            right=mid
        else:
            left=mid
    return right

N=8
a=[3,5,8,10,14,17,21,39]

a.append(float('infinity'))
a=[-1] + a

#このとき重要な性質としてアルゴリズムの初期状態から終了状態まで，変数leftは常にfalse側，変数rightは常にtrue側にいる

print(binary_search(a,11)-1)
print(binary_search(a,14)-1)
print(binary_search(a,15)-1)
print(binary_search(a,39)-1)
print(binary_search(a,4)-1)
print(binary_search(a,40)-1)
print(binary_search(a,3)-1)
print(binary_search(a,2)-1)