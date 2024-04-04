class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        a={}
        l=len(A)
        for i in A:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        ans=[]
        for j in a:
            if a[j]>(l/3):
                ans.append(j)
        if len(ans)==0:
            return(-1)
        return(ans[0])