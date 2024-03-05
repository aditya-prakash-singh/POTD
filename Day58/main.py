class Solution:
    # @param A : string
     # @return an long
    def countSalutes(self, A):
        maxi=0
        ans=0
        for i in A:
            if i=='>':
                maxi+=1
            else:
                ans+=maxi
        return(ans)
