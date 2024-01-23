class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
        st=1
        for i in range(A-1):
            rd=str(st)
            prev=""
            ct=0
            new=""
            for j in rd:
                if j==prev:
                    ct+=1
                else:
                    new+=str(ct)+prev
                    ct=1
                    prev=j
            new+=str(ct)+prev
            st=int(new)
        return(st)
