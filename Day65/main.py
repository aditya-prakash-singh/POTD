class Solution:
	def removeNthFromEnd(self,A,B):
        curr=A
        l=0
        while(curr != None):
            l+=1
            curr=curr.next
        a=l-B+1
        prev=None
        curr=A
        for i in range(1,a):
            prev=curr
            curr=curr.next
        if(prev==None):
            A=A.next
            return A
        else:
            prev.next=prev.next.next
            return A