# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def merge(s, e):
    dummy = ListNode(0)
    current = dummy
    while s and e:
        if s.val < e.val:
            current.next = s
            s = s.next
        else:
            current.next = e
            e = e.next
        current = current.next
    if s:
        current.next = s
    if e:
        current.next = e
    return dummy.next
	
def find_middle(A):
    slow = A
    fast = A.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
	
def kom(A):
    if not A or not A.next:
        return A
    a = find_middle(A)
    b = a.next
    a.next = None
    s=kom(A)
    e=kom(b)
    ans=merge(s,e)
    return ans
class Solution:
    def sortList(self, A):
        return kom(A)