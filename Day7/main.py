class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        fq={}
        for i in A:
            if i not in fq:
                fq[i]=1
            else:
                fq[i]+=1
        abc=0
        for i in fq:
            if fq[i]%2!=0:
                abc+=1
        if len(A)%2==0 and abc==0:
            return(1)
        elif len(A)%2==1 and abc==1:
            return(1)
        else:
            return(0)
