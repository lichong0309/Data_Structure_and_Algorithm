'''
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

 

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]


示例 2：
输入：root = [2,1,3]
输出：[2,3,1]


示例 3：
输入：root = []
输出：[]
 

提示：

树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from typing import Optional

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 如果树为空
        if root == None:
            return root
        # 如果是叶子节点，则直接返回
        if root.left == None and root.right == None:
            return root
        else:
            leftNode = self.invertTree(root.left)
            rightNode = self.invertTree(root.right)
            # 交换
            root.left, root.right = root.right, root.left
            return root 


            
            
