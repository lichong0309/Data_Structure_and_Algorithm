'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
 

示例 1：

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true


示例 2：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109
'''
from typing import List
class Solution:
    def help(self, matrix, i, j, target):
        m = len(matrix)
        if i >= m or j < 0:
            return False
        else:
            if target == matrix[i][j]:
                return True 
            else:
                if target > matrix[i][j]:
                    res = self.help(matrix, i+1, j, target)
                else:
                    res = self.help(matrix, i, j-1, target)
            return res
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 从右上角，可以看做是一个 搜索二叉树
        # m = len(matrix)
        n = len(matrix[0])
        ans = self.help(matrix, 0, n-1, target)
        return ans 
