class Solution:
    # @param A: tuple of integers
    # @return: an integer
    def repeatedNumber(self, A):
        a = A[0]
        b = A[0]
        while True:
            a = A[a]
            b = A[A[b]]
            if a == b:
                break
        a = A[0]
        while a != b:
            a = A[a]
            b = A[b]
        return a
