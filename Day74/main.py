# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
		if A.next==None:
			return(A)
		cur=A
		prev=cur
		l=0
		while(cur!=None):
			l+=1
			prev=cur
			cur=cur.next
		cur=A
		B=B%l
		if B==0:
			return(A)
		for i in range(l-B-1):
			cur=cur.next
		ans=cur.next
		cur.next=None
		prev.next=A
		return(ans)
		
