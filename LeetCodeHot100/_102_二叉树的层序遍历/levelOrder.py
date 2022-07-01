
'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]
 

提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 如果二叉树为空
        if root == None:
            return []
            
        ans = []        # 存放结果
        nextLevel = [root]          # 初始化nextLevel为第一层的节点

        # 循环所有层
        while nextLevel != []:
            curLeverl = nextLevel   # 当前层的节点集合
            curVal = []             # 存放当前层的节点的值
            nextLevel = []          # 重置下一层节点的集合
            
            # 循环当前层的每个节点，将当前节点的子节点添加到下一层的集合中
            while curLeverl != []:
                cur = curLeverl.pop(0)
                curVal.append(cur.val)          # 将节点的val添加到list中
                # 将本层的节点的子节点加到下一层中
                if cur.left != None:
                    nextLevel.append(cur.left)
                if cur.right != None:
                    nextLevel.append(cur.right)
            
            # 将本层的值添加到结果中
            ans.append(curVal)
        return ans 