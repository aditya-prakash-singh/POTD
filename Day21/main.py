def check(a,b):
    ct=0
    for i in range(min(len(a),len(b))):
        if a[i]==b[i]:
            ct+=1
        else:
            return(a[:ct])
    return(a[:ct])
class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        st=A[0]
        for i in range(1,len(A)):
            st=check(st,A[i])
        return(st)
