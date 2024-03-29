# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		a={A.val:0}
		curr=A.next
		prev=A
		while(curr!=None):
			if curr.val not in a:
				a[curr.val]=1
				prev.next=curr
				prev=curr
			curr=curr.next
		prev.next=curr
		return(A)