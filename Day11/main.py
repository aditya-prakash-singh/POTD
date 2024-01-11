class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        st=''
        for i in A:
            st+=str(i)
        st=str(int(st)+1)
        B=[]
        for i in range(len(st)):
            B.append(int(st[i]))
        return(B)
