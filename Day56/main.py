class Solution:
    # @param A : list of strings
    # @return a strings
    def serialize(self, A):
        ans=""
        for i in A:
            ans+=i+str(len(i))+'~'
        return(ans)
