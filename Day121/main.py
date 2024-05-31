class Solution:
    def swapNibbles (self, n):
        return(((n&15)*(1<<4))+(n>>4)); 