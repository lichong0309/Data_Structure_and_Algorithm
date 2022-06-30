'''
给你两棵二叉树： root1 和 root2 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。

示例 1：
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]

示例 2：
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
 

提示：

两棵树中的节点数目在范围 [0, 2000] 内
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 方法一：使用递归

        # 如果root1和root2其中一个为None，则返回另外一个节点
        if root1 == None:
            return root2
        elif root2 == None:
            return root1
        
        # root1和root2都不为None
        else:
            # 创建新节点
            newNode = TreeNode(root1.val + root2.val)
            newNode.left = self.mergeTrees(root1.left, root2.left)
            newNode.right = self.mergeTrees(root1.right, root2.right)
            return newNode

        
        # # 方法二：
        # # 使用广度优先遍历
        # # 将root1没有，root2有的子树，链接到root1，并且root1和root2都不需要遍历这一部分
        # # 将root1和root2都存在的子树的每个节点的数据进行相加，同时遍历这一部分
        # if root1 == None:
        #     return root2
        # elif root2 == None:
        #     return root1
        # else:
        #     queue1 = []         # root1的队列
        #     queue2 = []         # root2的队列
        #     queue1.append(root1)
        #     queue2.append(root2)
        #     while queue1 != [] and queue2 != []:
        #         cur1 = queue1.pop(0)
        #         cur2 = queue2.pop(0)

        #         # root1和root2都有的节点，每个节点的数据进行相加，同时遍历他们的左右子树
        #         cur1.val += cur2.val

        #         # 左孩子
        #         # 如果root1和root2的左孩子都有，则遍历这一部分
        #         if cur1.left != None and cur2.left != None:
        #             queue1.append(cur1.left)
        #             queue2.append(cur2.left)
                
        #         # 如果root1的左孩子没有，root2的左孩子有，则将root2的左孩子复制添加到root1中，不遍历这一部分，因为他们的值不需要再次相加
        #         elif cur1.left == None and cur2.left != None:
        #             cur1.left = cur2.left 
                
        #         # 如果root1的左孩子有， root2的左孩子没有，则root1和root2的左孩子都不需要遍历，因为root1的这一部分不需要相加，同时因为返回的是root1，所以也不需要复制到root2中
        #         # 如果root1和root2的左孩子都没有，则不需要遍历他们的左孩子
        #         else:
        #             pass

        #         # 右孩子
        #         # 同理左孩子
        #         if cur1.right != None and cur2.right != None:
        #             queue1.append(cur1.right)
        #             queue2.append(cur2.right)
        #         elif cur1.right == None and cur2.right != None:
        #             cur1.right = cur2.right
        #         else:
        #             pass

        # # 返回root1
        # return root1
            
