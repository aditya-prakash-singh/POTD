class Solution:
    def recamanSequence(self, n):
        a = [0] * n
        b = set()
        for i in range(1, n):
            a[i] = a[i-1] - i
            if a[i] <= 0 or a[i] in b:
                a[i] = a[i-1] + i
            b.add(a[i])
        return a
