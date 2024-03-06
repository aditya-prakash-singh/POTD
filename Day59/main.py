class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        a={}
        for i in A:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        ans=""
        for i in a:
            ans+=i+str(a[i])
        return(ans)
