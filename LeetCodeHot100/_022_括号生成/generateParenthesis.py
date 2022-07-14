'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]
 
提示：
1 <= n <= 8
'''

from typing import List
class Solution:

    def dfs(self, n, path, left, right, ans):
        """回溯法，深度优先遍历，递归

        Args:
            n (_type_): 生成括号的对数
            path (_type_): 生成括号的组合
            left (_type_): 左括号在path中的个数
            right (_type_): 右括号在path中的个数
            ans (_type_): 存储有效的括号组合
        """
        # 退出条件 1) 如果左括号大于n，则不符合条件
        #         2) 如果右括号多于左括号，则不符合条件
        if left > n or right > left:
            return 

        # 退出条件  3） 如果左右括号之和等于2*n,则作为有效的括号组合添加到ans中
        if len(path) == 2 * n:
            ans.append(path)
            return 
        
        # 递归
        self.dfs(n, path+'(', left+1, right, ans)
        self.dfs(n, path+')', left, right+1, ans)    

    def generateParenthesis(self, n: int) -> List[str]:
        # 使用回溯法，深度优先遍历
        # 可以抽象成完全二叉树，左孩子是‘(’,右孩子是“)”
        # 完全二叉树的每条path 即是 组成的 括号组合 的一个例子，但需要找到有效的括号组合
        ans = []
        path = ''
        self.dfs(n, path, 0, 0 ,ans)
        return ans 