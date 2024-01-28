class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def check(a, s, e):
            while s < e:
                if a[s] != a[e]:
                    return 0
                s += 1
                e -= 1
            return 1
        s = 0
        e = len(A) - 1
        while s < e:
            if A[s] != A[e]:
                return check(A, s + 1, e) or check(A, s, e - 1)
            s += 1
            e -= 1
        return 1
