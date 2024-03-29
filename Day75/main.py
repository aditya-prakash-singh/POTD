# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        slow=fast=A
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        count=0
        cur=A
        while cur!=slow:
            count+=1
            cur=cur.next
        
        target_position = count - B
        
        if target_position < 0:
            return -1
        
        cur = A
        for _ in range(target_position):
            cur = cur.next
        
        return cur.val