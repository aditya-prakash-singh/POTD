class Solution:
    def solve(self, A, B):
        todo = []
        st = A[0]
        ct = 1
        bef = 0
        i = 0 
        for i in range(len(A)):
            if A[i] == st:
                ct += 1
            else:
                if (i - bef) == B:
                    todo.append(bef)
                st = A[i]
                ct = 1
                bef = i
        if (i - bef + 1) == B:
            todo.append(bef)
        count = 0
        for j in todo:
            A = A[:j - (count * B)] + A[j - (count * B) + B:]
            count += 1
        return A
