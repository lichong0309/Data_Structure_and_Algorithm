'''
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。

 

示例 1:



输入: root = [2,1,3]
输出: 1
示例 2:



输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 

提示:

二叉树的节点个数的范围是 [1,104]
-231 <= Node.val <= 231 - 1 

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, max_depth, depth, ans):
        if root == None:
            return max_depth, ans
        else:
            depth += 1
            if depth > max_depth:
                max_depth = depth 
                ans = root.val
            else:
                pass
            max_depth, ans = self.dfs(root.left, max_depth, depth, ans)
            max_depth, ans = self.dfs(root.right, max_depth, depth, ans)
            return max_depth, ans 

    def findBottomLeftValue(self, root: TreeNode) -> int:
        # # 使用层序遍历
        # queue = []
        # queue.append(root)
        # while queue != []:
        #     cur = queue.pop(0)
        #     if cur.right != None:
        #         queue.append(cur.right)
        #     else:
        #         pass
        #     if cur.left != None:
        #         queue.append(cur.left)
        # return cur.val
        

        # 使用递归
        max_depth, ans = self.dfs(root, 0, 0, root.val)
        return ans