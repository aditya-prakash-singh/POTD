class Solution:
	def lPalin(self, A):
        s=[]
        while(A!=None):
            s.append(A.val)
            A=A.next
        if s==s[::-1]:
            return(1)
        return(0)
