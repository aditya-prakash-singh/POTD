class Solution:
	# @param A : string
	# @return an integer
	def atoi(self, A):
		s = A.lstrip() 
		sign = 1
		if s and (s[0]=='-' or s[0]=='+'):
			sign = -1 if s[0]=='-' else 1
			s = s[1:]
		ans=0
		for i in s:
			if i.isdigit():
				a = int(i)
				if ans>(2147483647-a)//10:
					return 2147483647 if sign == 1 else -2147483648
				ans = ans * 10 + a
			else:
				break 
		return sign * ans
