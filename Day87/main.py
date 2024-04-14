class Solution:
    # @param A : string
    # @return a string
    def simplifyPath(self, A):
        kom=[]
        a=A.split("/")
        for i in a:
            if i==".." and kom:
                kom.pop()
            elif i!="." and i!='' and i!='..':
                kom.append(i)
        return "/" + "/".join(kom)