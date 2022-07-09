'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true


示例 2：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
 

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
'''



from typing import List
class Solution:
    def help(self, board, word, visited, i, j, pos, ans):
        # 如果超出了边界：
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return ans 
        # 如果board[i][j]当前元素 不等于 word的当前元素
        elif board[i][j] != word[pos]:
            return ans 
        # 如果被访问过了
        elif visited[i][j] == True:
            return ans
        # 如果遍历的结果已经符合要求
        elif pos == (len(word)-1):
            return True
        else:
            visited[i][j] = True 
            # 向上
            up_ans = self.help(board, word, visited, i-1, j, pos+1, ans)
            # 向下：
            down_ans = self.help(board, word, visited, i+1, j, pos+1, ans)
            # 向左：
            left_ans = self.help(board, word, visited, i, j-1, pos+1, ans)
            # 向右：
            right_ans = self.help(board, word, visited, i, j+1, pos+1, ans)
            # print(up_ans, down_ans, left_ans, right_ans)
            ans = up_ans or down_ans or left_ans or right_ans
            if ans == False:
                visited[i][j] = False
            return ans 


    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1.找到起始点：遍历整个二维数组
        # 2.遍历每个节点的上下左右
        rows = len(board)
        colums = len(board[0])

        # 遍历二维数组，作为起始点
        for i in range(rows):
            for j in range(colums):

                pos = 0
                ans = False 
                visited = [[False] * colums for _ in range(rows)]

                ans = self.help(board, word, visited, i, j, pos, ans)

                if ans == True:
                    return ans 
                else:
                    pass

        return ans 

