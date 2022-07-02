'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：
树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 得到节点p的父节点，并存放到list中
    def help(self, root, p, pList):
        """_summary_

        Args:
            root (_type_): 子树根节点
            p (_type_): 需要寻找的节点
            pList (_type_): 存放节点p父节点的list

        Returns:
            bool: _description_
        """
        
        if root == None:
            return False
        else:
            # 如果找到了p， 则返回True
            if root.val == p.val:
                pList.append(root)
                return True

            Inleft = self.help(root.left, p, pList)
            Inright = self.help(root.right, p, pList)

            # 如果root的左子树或者右子树存在p，则root为p节点的祖先节点
            # 将root加入list中进行保存，返回True
            # 否则返回False
            if Inleft == True or Inright == True:
                pList.append(root)      
                return True
            else:
                return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 将p和q的父节点存放到list中
        # 分别比较两个list
        
        pList = []                  # 存放p节点的祖先节点
        qList = []                  # 存放q节点的祖先节点

        self.help(root, p, pList)   # 得到p节点的祖先节点
        self.help(root, q, qList)   # 得到q节点的祖先节点
        # print(pList, qList)

        # for i in range(len(pList)):
        #     print(pList[i].val)
        
        # for i in range(len(qList)):
        #     print(qList[i].val)

        i = 0 
        while pList[i] not in qList:
            i = i + 1
        return pList[i]



        


