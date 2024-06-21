class Solution:
    def compareFrac(self, s):
        a, b = s.strip().split()
        a = a.strip(',')
        c, d = a.split('/')
        e, f = b.split('/')
        if int(c)/int(d) > int(e)/int(f):
            return a
        elif int(c)/int(d) == int(e)/int(f):
            return "equal"
        else:
            return b