# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        cur=ListNode(0)
        cur.next=A
        prev=cur
        for _ in range(B-1):
            prev=prev.next        
        curr=prev.next
        next_node=curr.next
        for _ in range(C-B):
            temp=next_node.next
            next_node.next=curr
            curr=next_node
            next_node=temp
        prev.next.next=next_node
        prev.next=curr
        return cur.next