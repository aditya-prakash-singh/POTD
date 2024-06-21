class Solution:
    def ExtractNumber(self,sentence):
        a=sentence.split()
        ans=-10e19
        for i in a:
            if i.isdigit():
                if '9' not in str(i):
                    ans=max(ans,int(i))
        if ans!=-10e19:
            return(ans)
        return(-1)