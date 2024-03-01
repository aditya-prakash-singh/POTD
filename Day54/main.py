class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def addNumbers(self, A, B):
        # return(A+B), 2 min me ho gaya
        # galti se ye use kardiya tha isliye 
        while(B!=0):
            A,B=(A^B),((A&B)<<1)
        return(A)
