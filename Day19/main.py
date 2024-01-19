class Solution:
	# @param A : integer
	# @return a strings
	def intToRoman(self, A):
        a = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
        b = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        ans=""
        while A:
            c = A // a[i]
            A %= a[i]
            ans+=b[i]*c
            i -= 1
        return(ans)
