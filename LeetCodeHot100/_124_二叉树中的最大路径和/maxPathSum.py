'''
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
 

示例 1：

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def help(self, root, max_sum_156):
        # 如果是叶子节点
        if root.left == None and root.right == None:
            return max_sum_156, root.val

        # 如果只有左孩子
        elif root.left != None and root.right == None:
            _max_sum_156, left = self.help(root.left, max_sum_156)
            max_sum_156 = max(max_sum_156, _max_sum_156)
            max_sum_156 = max(max_sum_156, left)
            max_sum_234 = max(root.val+left, root.val)
            return max_sum_156, max_sum_234
        
        # 如果只有右孩子
        elif root.left == None and root.right != None:
            _max_sum_156, right = self.help(root.right, max_sum_156)
            max_sum_156 = max(max_sum_156, _max_sum_156)
            max_sum_156 = max(max_sum_156, right)
            max_sum_234 = max(root.val+right, root.val)
            return max_sum_156, max_sum_234

        # 如果左孩子和右孩子都有
        else:
            left_max_sum_156, left = self.help(root.left, max_sum_156)
            right_max_sum_156, right = self.help(root.right, max_sum_156)
            max_sum_156 = max(max_sum_156, left_max_sum_156, right_max_sum_156)
            max_sum_156 = max(max_sum_156, root.val+left+right, left, right)
            max_sum_234 = max(root.val+left, root.val+right, root.val)
            return max_sum_156, max_sum_234

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # 思路： 对于一个颗子树来说，最大路径和只存在以下六种可能：
        # 1. root + left + right
        # 2. root + left
        # 3. root + right
        # 4. root
        # 5. left
        # 6. right
        # 使用全局变量记录 1， 5， 6 三种情况的最大值, 因为这三种情况不能向上累加,为每个节点所单独拥有的属性
        #      并在所有节点的该属性中找到最大的一个，max_sum_156
        # 递归遍历整个树 得到 2， 3， 4 三种情况的最大值，这三种情况需要向上累加, 迭代累加到root节点即为在该
        #      情况下的最大值 ，max_max_234
        
        max_sum_156 = float("-inf")
        max_sum_156, max_sum_234 = self.help(root, max_sum_156)
        maxNum = max(max_sum_156, max_sum_234)
        return maxNum
