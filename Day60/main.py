class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        a,ans=[],0
        for i in A:
            if i=='(':
                a.append(i)
            elif i==')':
                if not a:
                    ans+=1
                else:
                    a.pop()
        return ans+len(a)
