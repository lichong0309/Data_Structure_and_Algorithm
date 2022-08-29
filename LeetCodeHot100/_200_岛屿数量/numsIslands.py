'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
'''

from typing import List

class Solution:
    def dfs(self, x, y, grid):
        m = len(grid) - 1 
        n = len(grid[0]) - 1 
        # 判断是否越界
        if x < 0 or x > m or y < 0 or y > n:
            return 
        # 如果不是1：
        elif grid[x][y] != "1":
            return 
        else:
            grid[x][y] = "0"
            self.dfs(x, y-1, grid)
            self.dfs(x, y+1, grid)
            self.dfs(x-1, y, grid)
            self.dfs(x+1, y, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        # 思路：递归进行深度优先搜索
        # 1. 通过深度优先搜索将1的上下左右四个方向的1的数量标记为0
        # 2. 将1的位置标记为0，防止重新计数

        ans = 0
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    self.dfs(x, y, grid)
                    ans += 1 
                else:
                    pass

        return ans