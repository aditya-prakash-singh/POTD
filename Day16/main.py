class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
        a=list(A.split(" "))
        for i in range(len(a)-1,-1,-1):
            if a[i]!="":
                return(len(a[i]))
        return(0)      
