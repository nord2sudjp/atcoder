 N=int(input())
 *A,=list(map(int,input().split()))
 ans=0
 for l in range(N):
     cnt=x=A[l]
     r=l+1
     while r<N and a<=A[r]:
             # l�͌Œ肵�Ă���B
             # ����l�ɑ΂���r��r<l�ƂȂ������_�ŒT������߂Ă���
             # ���������ۂɂ�l��r�̂��ׂĂ̑g�ݍ��킹�ɂ��Ă��̒��ł̍ŏ��l�����߂�̂�������
         cnt+=x # �����͊|���Z�ɂł���
         r+=1
     print(l+1,r,A[l],cnt,ans)
     ans=max(ans,cnt)
 print(ans)           