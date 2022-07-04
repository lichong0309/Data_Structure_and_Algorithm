'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6
 
提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # 方法一，动态规划
        # dp = [[0] * n  for _ in range(m)]

        # for i in range(m):
        #     # 如果是第一行, 则为1
        #     if i == 0:
        #         for j in range(n):
        #             dp[i][j] = 1
        #     # 如果不为第一行
        #     else:
        #         for j in range(n):
        #             # 如果为第一列
        #             if j == 0:
        #                 dp[i][j] = 1
        #             # 如果不为第一列
        #             # 则到达第i行第j列的最多路径为 从上边的路径 + 从左边来的路径
        #             # dp[i-1][j]：从上边 来的 路径
        #             # dp[i][j-1]: 从左边 来的 路径
        #             else:
        #                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        # return dp[m-1][n-1]

        # 方法二， 数学公式
        import math
        M = m - 1 
        N = m + n - 2 
        ans = math.factorial(N) / (math.factorial(N-M) * math.factorial(M))
        return int(ans)

        