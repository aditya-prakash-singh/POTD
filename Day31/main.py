class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        a = "abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        for i in a:
            if i not in s:
                return False
        return True
