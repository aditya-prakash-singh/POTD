class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        result = [0] * (n - 2)
        for i in range(0, n - 2):
            result[i] = [0] * (n - 2)
        
        for i in range(0, n - 2):
            for j in range(0, n - 2):
                cur_max = 0
                for k in range(0, 3):
                    for l in range(0, 3):
                        if grid[k + i][l + j] > cur_max:
                            cur_max = grid[k + i][l + j]
                result[i][j] = cur_max
        return result