class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        v=['a','e','i','o','u','A','E','I','O','U']
        a,b,c,d,ans,l=[],[],0,0,0,len(A)
        for i in range(l-1,-1,-1):
            if A[i] in v:
                c+=1
            else:
                d+=1
            a.append(c)
            b.append(d)
        a=a[::-1]
        b=b[::-1]
        for i in range(l):
            if A[i] in v:
                ans+=b[i]
            else:
                ans+=a[i]
        return(ans%1000000007)
