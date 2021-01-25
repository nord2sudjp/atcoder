 N=int(input())
 *A,=list(map(int,input().split()))
 ans=0
 for l in range(N):
     cnt=x=A[l]
     r=l+1
     while r<N and a<=A[r]:
             # l‚ÍŒÅ’è‚µ‚Ä‚¢‚éB
             # ‚»‚Ìl‚É‘Î‚·‚ér‚Ír<l‚Æ‚È‚Á‚½“_‚Å’Tõ‚ğ‚â‚ß‚Ä‚¢‚é
             # ‚µ‚©‚µÀÛ‚É‚Íl‚Ær‚Ì‚·‚×‚Ä‚Ì‘g‚İ‡‚í‚¹‚É‚Â‚¢‚Ä‚»‚Ì’†‚Å‚ÌÅ¬’l‚ğ‹‚ß‚é‚Ì‚ª³‚µ‚¢
         cnt+=x # ‚±‚±‚ÍŠ|‚¯Z‚É‚Å‚«‚é
         r+=1
     print(l+1,r,A[l],cnt,ans)
     ans=max(ans,cnt)
 print(ans)           