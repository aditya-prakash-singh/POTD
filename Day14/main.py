class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        st=""
        for i in A:
            if i.isalpha():
                st+=i.lower()
            elif i.isdigit():
                st+=str(i)
        if st[::-1]==st:
            return(1)
        return(0)
