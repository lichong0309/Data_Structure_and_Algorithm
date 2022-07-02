'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:
二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
class Solution:
    
    def help(self, root, targetSum):
        if root == None:
            return 0
        else:
            ans = 0 
            ans += self.help(root.left, targetSum - root.val)
            ans += self.help(root.right, targetSum - root.val)

            # 如果root本身也符合条件，则加一
            if root.val == targetSum:
                ans += 1   
                
            return ans 
    
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 双重迭代遍历
        if root == None:
            return 0 
        else:
            
            # 判断root子树是否存在符合条件的路径
            # 需要使用迭代
            ans = self.help(root, targetSum)

            # 对于整颗二叉树的每个节点
            # 都有可能和他们的子树的某些节点组成符合条件的路径
            # 所以需要对每个节点进行遍历
            ans += self.pathSum(root.left, targetSum)
            ans += self.pathSum(root.right, targetSum)

            return ans 