class Solution:
    def deleteDuplicates(self, A):
        if A is None or A.next is None:
            return A
        cur=ListNode(0)
        cur.next=A
        prev=cur
        curr=A
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return cur.next