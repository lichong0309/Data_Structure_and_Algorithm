'''
114. 二叉树展开为链表
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
 
提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100
 

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？


'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        # """
        # Do not return anything, modify root in-place instead.
        # """
        
        
        # 如果二叉树为空时
        if root == None:
            return 

        # 当root为叶子结点时
        if root.left == None and root.right == None:
            return 
        else:
            if root.left:
                self.flatten(root.left)
            if root.right:
                self.flatten(root.right)

            # 如果存在左子树，则插入到右子树中，防止左子树为空插入右子树后导致右子树丢失
            if root.left != None:
                # 将root的左子树插入到右子树中
                cur = root              # 遍历左子树
                temp = root.right       # 暂存（拉住）root的右子树

                # while循环结束后，cur将指向左子树的叶子节点 或者 没有左子树时的root子树的叶子节点
                while cur.left != None or cur.right != None:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur = cur.right

                # 将左子树插入右子树中
                root.right = root.left      # root链接左子树为右子树
                cur.right = temp             # 新的右子树的最后一个节点指向 原来的右子树
                
                # 将root的左子树置为空
                root.left = None
    
    
    
    
        # # 方法二：将右子树搬到左子树中，再将左子树移动到右子树中

        # cur = root 

        # while cur != None:

        #     # 移动到root节点的左子树的第一个节点
        #     if cur.left != None:
        #         leftFirst = cur.left

        #         # 从leftFirst开始寻找 最右节点
        #         cur1 = leftFirst 
        #         while cur1.right != None:
        #             cur1 = cur1.right
                
        #         # 循环结束后cur1为 最右节点
        #         # 将root的右子树搬到 左子树 的 最右节点上
        #         cur1.right = cur.right

        #         # 将左子树移动到右子树
        #         cur.right = cur.left 
                
        #         # 左子树设为None
        #         cur.left = None 

        #     # cur移动到一个右节点
        #     cur = cur.right 

