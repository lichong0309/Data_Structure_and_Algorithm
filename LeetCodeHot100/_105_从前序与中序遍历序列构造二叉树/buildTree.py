'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]


示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]
 

提示:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if preorder == [] or inorder == []:
            return None 

        elif preorder != [] and inorder != []:
            rootVal = preorder[0]                                 # 得到root的值

            root = TreeNode(val=rootVal)                          # 根据root的值创建root节点

            rootIndex = inorder.index(rootVal)                    # 得到root的索引

            leftInOrder = inorder[0:rootIndex]                    # left:中序遍历
            rightInOrder = inorder[rootIndex+1:]                  # right:中序遍历
            leftPreOrder = preorder[1:len(leftInOrder)+1]         # left:前序遍历
            rightPreOrder = preorder[len(leftInOrder)+1:]         # right:前序遍历
            # print(leftPreOrder,leftInOrder, rightPreOrder,rightInOrder)


            leftNode = self.buildTree(leftPreOrder, leftInOrder)
            rightNode = self.buildTree(rightPreOrder, rightInOrder)

            # 加入left和right到root
            root.left = leftNode
            root.right = rightNode

        return root