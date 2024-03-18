class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        s=''
        for i in A:
            s+=i
        for i in range(97,123):
            if chr(i) not in s:
                return(0)
        return(1)