class Solution:
	# @param A : string
	# @return an integer
	def power(self, A):
		A=int(A)
		while(A%2==0 and A!=2):
			A=A//2
		return 1 if A==2 else 0
		
