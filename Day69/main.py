class Solution:
    def swapPairs(self, A):
        if not A or not A.next:
            return A
        prev=None
        cur=A
        while cur and cur.next:
            a=cur
            b=cur.next
            cur=b.next
            a.next=cur
            b.next=a
            if prev:
                prev.next=b
            else:
                A=b
            prev=a
        return A