class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        a=A.split(' ')
        while(' ' in a):
            a.remove(' ')
        while('' in a):
            a.remove('')
        return(len(a))
