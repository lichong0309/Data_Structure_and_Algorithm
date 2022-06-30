'''

给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true


示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
 

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
 
进阶：你可以运用递归和迭代两种方法解决这个问题吗？

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归
        # 设计两个指针，分别在整棵树从根节点开始向左右子树移动
        # 将根节点的左右子树分为两颗树
        ans = self.check(root.left, root.right)
        return ans 

    def check(self, root1, root2):
        # 如果root1 和 root2都为None，则符合对称，返回True
        if root1 == None and root2 == None:
            return True

        # 如果root1 和 root2都不为None,则判断他们的值是否相等
        elif root1 != None and root2 != None:
            # 如果root1 和 root2的值相等，则root1和root2向下遍历
            if root1.val == root2.val:
                res1 = self.check(root1.left, root2.right)
                res2 = self.check(root1.right, root2.left)
                # 如果 root1和root2的左右子树都对称，则返回True
                if res1 == True and res2 == True:
                    return True
                else:
                    return False
            # 如果root1和root2的值不相等，则返回False
            else:
                return False
        # 如果root1和root2其中一方为None，另一方不为None，则返回False.
        else:
            return False


