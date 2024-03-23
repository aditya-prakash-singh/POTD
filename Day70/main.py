# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None
        a=A
        b=B
        while a!=b:
            a=a.next if a else B
            b=b.next if b else A
        return a
