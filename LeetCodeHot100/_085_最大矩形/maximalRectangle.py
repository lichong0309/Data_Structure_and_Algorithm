'''
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 
示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
 

提示：
rows == matrix.length
cols == matrix[0].length
1 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'

'''

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows == 0:
            return 0

        sequentOneMatrix = [[0]*cols for i in range(rows)]

        for i in range(rows):
            if matrix[i][0] == "1":
                sequentOneMatrix[i][0] = 1

        # 给sequentOneMatrix赋值
        # sequentOneMatrix[i][j]表示第i行第j列的元素的左边连续1的数量
        for i in range(rows):
            for j in range(1, cols):
                if matrix[i][j] == "0":
                    sequentOneMatrix[i][j] = 0
                else:
                    sequentOneMatrix[i][j] = sequentOneMatrix[i][j-1] + 1
        
        ans = 0
        # 计算以第i行第j列作为右下角能组成的最大矩形
        for i in range(rows):               # 横向遍历
            for j in range(cols):           # 纵向遍历
                width = sequentOneMatrix[i][j]
                count = 1
                area = width * count 
                # 如果第i行第j列为0
                if matrix[i][j] == "0":
                    continue 
                
                else:
                    n = i - 1
                    while n >= 0:
                        if sequentOneMatrix[n][j] > width:
                            count = count + 1
                            new_area = width * count 
                            area = max(area, new_area)
                        else:
                            count = count + 1
                            width = sequentOneMatrix[n][j]
                            new_area = width * count 
                            area = max(area, new_area)
                        n = n - 1
                
                ans = max(ans, area)
        return ans 
        
                