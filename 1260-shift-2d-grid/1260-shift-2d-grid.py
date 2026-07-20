class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def shift_2d_grid(a: List[List[int]]) -> List[List[int]]:
            b = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n-1):
                    b[i][j+1] = a[i][j]
            
            for i in range(m-1):
                b[i+1][0] = a[i][n-1]
            
            b[0][0] = a[m-1][n-1]
            return b
                    
        for _ in range(k):
            grid = shift_2d_grid(grid)

        return grid