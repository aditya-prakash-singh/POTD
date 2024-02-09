class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
		ans=0
		for i in range(len(A)):
			ct=0
			s=set()
			for j in range(i,len(A)):
				c=A[j]
				if c in s: 
					break
				s.add(c)
				ct+=1
			ans=max(ans,ct)
		return ans
