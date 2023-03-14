class Solution:
    def minPathSum(self, grid) -> int:
        # 方法二： 动态规划

        grid_m = len(grid) 
        grid_n = len(grid[0])

        # 创建二维数组
        dp = [[0] * grid_n for _ in range(grid_m)]

        # dp[0][0] = grid[0][0]
        
        # 对于每行
        for i in range(grid_m):
            # 如果为第一行，只需要加上从左来的值
            if i == 0:
                for j in range(grid_n):
                    print(dp[i][j-1])
                    dp[i][j] = grid[i][j] + dp[i][j-1]
            # 如果不为第一行，则需要加上从左来的值 和 从上来的值
            else:
                for j in range(grid_n):
                    # 如果为第一列，只需要加上从上来的值
                    if j == 0:
                        # print(dp[])
                        dp[i][j] = grid[i][j] + dp[i-1][j]

                    # 如果不为第一列，则需要比较是加上从上来的值 还是 从左来得值
                    else:
                        # 如果 从 左 来的值
                        left = grid[i][j] + dp[i][j-1]
                        # 如果 从 上 来的值
                        up = grid[i][j] + dp[i-1][j]

                        if left >= up:
                            dp[i][j] = up
                        else:
                            dp[i][j] = left
        # print(dp)
        return dp[grid_m-1][grid_n-1]  

    # # 方法一：使用递归， 超时
    # # 建模成二叉树， 寻找节点值最小的path
    # def help(self, grid, m, n):
    #     grid_m = len(grid) - 1
    #     grid_n = len(grid[0]) - 1

    #     if m >= grid_m and n >= grid_n:
    #         return grid[grid_m][grid_n]
        
    #     else:
    #         leftCount = 0
    #         rightCount = 0
    #         # 可以向下
    #         if m < grid_m:
    #             leftCount = self.help(grid, m+1, n)
    #         if n < grid_n:
    #             rightCount = self.help(grid, m, n+1)
            
    #         if leftCount == 0:
    #             minNum = rightCount
    #         elif rightCount == 0:
    #             minNum = leftCount
    #         else:
    #             minNum = min(leftCount, rightCount)
    #         return grid[m][n] + minNum

    # def minPathSum(self, grid: List[List[int]]) -> int:
        # ans = self.help(grid, 0, 0)
        # return ans

nums = [2,1,5,6,2,3]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
ans = s.minPathSum(grid)
print(ans)