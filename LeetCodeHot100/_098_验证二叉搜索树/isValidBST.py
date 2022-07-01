'''

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

示例 1：
输入：root = [2,1,3]
输出：true


示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
 
提示：
树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def help(self, root, lower, upper):
        """_summary_

        Args:
            root (TreeNode): 节点
            lower (int): 节点的值所能允许的最小值
            upper (int): 节点的值所能允许的最大值

        Returns:
            bool: True:则是搜索二叉树， False:不是搜索二叉树
        """
        if root == None:
            return True
        else:
            if root.val > lower and root.val < upper:
                leftIsValid = self.help(root.left, lower, root.val)
                rightIsValid = self.help(root.right, root.val, upper)
                rootIsValid = True
            else:
                return False

            if leftIsValid == True and rightIsValid == True and rootIsValid == True:
                return True 
            else:
                return False 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.help(root, -2**31-1, 2**31)
        return ans