class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        a={}
        ans1=0
        for i in A:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        b={}
        for i in range(len(B)):
            if A[i]!=B[i]:
                if B[i] not in b:
                    b[B[i]]=1
                else:
                    b[B[i]]+=1
            else:
                ans1+=1
                a[A[i]]-=1
        ans=0
        for j in a:
            if j in b:
                ans+=min(b[j],a[j])
        return(str(ans1)+'A'+str(ans)+'B')
