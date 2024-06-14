class Solution:
    def armstrongNumber (self, n):
        a = len(str(n))
        sumi = 0
        val = n
        while n != 0:
            sumi += (n%10)**a
            n = n//10
        return "true" if sumi == val else "false"