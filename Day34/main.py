def abc(word):
    a = {}
    for i in word:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    return a
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def permuteStrings(self, A, B):
        a=abc(A)
        b=abc(B)
        if a==b:
            return(1)
        else:
            return(0)
