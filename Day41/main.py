class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        a=[A,B,C,D]
        a.sort()
        if a[0]==a[1] and a[2]==a[3]:
            return(1)
        return(0)
