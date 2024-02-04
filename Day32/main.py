class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
		s=[]
		for i in A:
			s.append(i)
		ans=''
		while(len(s)):
			ans+=s.pop()
		return(ans)
