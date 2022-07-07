'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例 2：

输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
'''


from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 对于将元素作为正方形右下角 的宽取决于三个要素：
        # 1. 左上角的0的位置
        # 2. 右上角的0的位置
        # 3. 左下角的0的位置
        # 所以状态转移函数来源于三个方向
        # 1. 斜对角线，2. 上方， 3. 左方
        rows = len(matrix)                  # 行
        colums = len(matrix[0])             # 列

        dp = [[0]* colums for _ in range(rows)]

        max_width = 0
        for i in range(rows):
            for j in range(colums):
                if matrix[i][j] == "0":
                    continue
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 状态转移的来源
                        left = dp[i][j-1]
                        up = dp[i-1][j]
                        diagonal = dp[i-1][j-1]
                        dp[i][j] = min(left, up, diagonal) + 1
                    max_width = max(max_width, dp[i][j])
        ans = max_width * max_width
        return ans 