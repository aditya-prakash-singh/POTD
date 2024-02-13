class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):
		st=[-1]  
		ans=0
		for i in range(len(A)):
			if A[i]=='(':
				st.append(i)
			else:
				if st:
					st.pop()
					if st:
						ans=max(ans,i-st[-1])
					else:
						st.append(i)
				else:
					st.append(i)
		return ans
						
						
