class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ss0=students.count(0)
        ss1=students.count(1)
        for i in sandwiches:
            if i==0 and ss0>0:
                ss0-=1
            elif i==1 and ss1>0:
                ss1-=1
            else:
                break
        return ss0+ss1