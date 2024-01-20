class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
        i = 0
        b = 0
        while i < len(A):
            if i + 1 < len(A) and A[i:i + 2] in a:
                b += a[A[i:i + 2]]
                i += 2
            else:
                b += a[A[i]]
                i += 1
        return b
