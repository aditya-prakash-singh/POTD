class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=len(score)
        a=score.copy()
        a.sort(reverse=True)
        b={}
        for i in range(l):
            if i==0:
                b[a[i]]="Gold Medal"
            elif i==1:
                b[a[i]]="Silver Medal"
            elif i==2:
                b[a[i]]="Bronze Medal"
            else:
                b[a[i]]=str(i+1)
        ans=[]
        for i in score:
            ans.append(b[i])
        return(ans)