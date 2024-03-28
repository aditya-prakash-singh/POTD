# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        cur = A
        while cur:
            temp = (cur.val // B) * B
            if temp > cur.val:
                temp -= B
            cur.val = temp
            cur = cur.next
        return A