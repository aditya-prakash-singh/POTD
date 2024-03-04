class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        a=A.split('~')
        ans=[]
        for i in a:
            s=""
            for j in i:
                if j.isalpha():
                    s+=j
            ans.append(s)
        return ans[:-1]
