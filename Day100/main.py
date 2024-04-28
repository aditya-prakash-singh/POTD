class Solution:
    def subtract(self, A):
        def inverse_half(N, l):
            if l < 2:
                return N
            _cur = N.next
            _prev = N
            _next = _cur.next
            while (l - 1):
                _cur.next = _prev
                _prev = _cur
                _cur = _next
                _next = _next.next
                l -= 1
            N.next = _cur
            return _prev

        def sub_half(N, length):
            idx1 = N
            idx2 = N
            beginning_idx = 1 + length // 2 if (length % 2 == 1) else length // 2
            for _ in range(beginning_idx):
                idx2 = idx2.next
            for _ in range(length // 2):
                idx1.val = idx2.val - idx1.val
                idx1 = idx1.next
                idx2 = idx2.next
            return N

        length = 0
        p = A
        while (p != None):
            length += 1
            p = p.next
        A = inverse_half(A, length // 2)
        A = sub_half(A, length)
        return inverse_half(A, length // 2)
