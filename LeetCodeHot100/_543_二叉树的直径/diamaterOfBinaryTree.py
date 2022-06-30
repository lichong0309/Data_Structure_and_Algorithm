'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

注意：两结点之间的路径长度是以它们之间边的数目表示。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            # 得到左右子树的深度
            leftDepth = self.Depth(root.left)
            rightDepth = self.Depth(root.right)
            # 当前root的最大直径为：
            droot = leftDepth + rightDepth 
            # 得到当前root的左子树和右子树的最大直径
            dleft = self.diameterOfBinaryTree(root.left)
            dright = self.diameterOfBinaryTree(root.right)
            return max(droot, dleft, dright)
            
    def Depth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.Depth(root.left), self.Depth(root.right))
