'''


给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #  第一种方法：递归
    #     ans = []
    #     self.inorder(root, ans)
    #     return ans 

    # def inorder(self, root, ans):
    #     if root == None:
    #         return 
    #     else:
    #         self.inorder(root.left, ans)
    #         ans.append(root.val)
    #         self.inorder(root.right, ans)
    
    
    # 第二种方法：使用栈
        stack = []      # 初始化栈
        ans = []
        cur = root 
        while cur != None or stack != []:
            # 如果不为空，则一直压栈
            # 相当于 inorder(root.left) 或者 inorder(root.right)
            while cur != None:
                stack.append(cur)           # 压栈的是节点，方便后面找到父节点
                cur = cur.left 
            # 如果为cur为空，则说明cur的父节点没有左孩子，inorder(root.left)执行完成，转到inorder(root.right)
            # 此时cur为None，顶部元素退栈,即得到cur的父节点，父节点移动到右子树
            cur = stack.pop(-1)             # 得到父节点
            ans.append(cur.val)
            cur = cur.right                 # 移动到右子树
        
        return ans 
            

        