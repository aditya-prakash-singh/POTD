class Solution:
    def singleElement(self, arr, N):
        # code here 
        d = {}
        
        for i in range(N):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
           
        ans = sorted(d.items()) 
        for key, val in ans:
            if val == 1:
                return key
        
        return -1
