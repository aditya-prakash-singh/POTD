class Solution:
	def bracketNumbers(self, str):
		ans = []
        stack = []
        open_num = 1
        for x in str:
            if x == '(':
                ans.append(open_num)
                stack.append(open_num)
                open_num +=1
            if x == ')':
                ans.append(stack.pop())
        return ans