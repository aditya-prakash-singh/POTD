from typing import List

class Solution:
    def getPrimes(self, n):
        a = [True] * n
        p = 2
        while (p * p < n):
            if (a[p] == True):
                for i in range(p * p, n, p):
                    a[i] = False
            p += 1
        
        for i in range(2, n // 2 + 1):
            if a[i] and a[n - i]:
                return [i, n - i]
        
        return [-1, -1]