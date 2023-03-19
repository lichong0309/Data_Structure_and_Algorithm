from typing import List
class Solution:
    def dfs(self, grid, x, y):
        
        m = len(grid) - 1
        n = len(grid[0]) - 1

        if x < 0 or x > m or y < 0 or y > n:
            return 0 

        elif grid[x][y] == 0:
            return 0 

        else:
            area = 1
            grid[x][y] = 0 
            up_area = self.dfs(grid, x-1, y)
            down_area = self.dfs(grid, x+1, y)
            left_area = self.dfs(grid, x, y-1)
            right_area = self.dfs(grid, x, y+1)
            area = area + up_area + left_area + right_area + down_area
            return area



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0 
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i ,j)
                    ans = max(ans, area)

        return ans



