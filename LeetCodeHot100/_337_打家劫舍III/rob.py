'''
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
 
提示：
树的节点数在 [1, 104] 范围内
0 <= Node.val <= 104
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, i_list, non_list):
        """_summary_

        Args:
            root (_type_): 子树或者树 的根节点（父节点）
            i_list (_type_): 存放 各个 子树（树）选择 根节点（父节点）的最优解
            non_list (_type_): 存放 各个 子树（树）不选择 根节点（父节点）的最优解
        """
        if root == None:
            # non_list[root] = 0
            # i_list[root] = 0
            return 

        else:
            self.dfs(root.left, i_list, non_list)
            self.dfs(root.right, i_list, non_list)
            # 选择父节点的最优解
            # 如果选择父节点，则左右孩子节点都不能选择
            # 选择：当左右孩子节点不被选择时的最优解
            i_list[root] = root.val + non_list[root.left] + non_list[root.right]
            # 不选择父节点的最优解
            # 如果不选择父节点，对于左右孩子节点来说，可以选择，也可以不选择
            # max(左右孩子被选择， 左右孩子不被选择)
            non_list[root] = max(i_list[root.left], non_list[root.left]) + \
                             max(i_list[root.right], non_list[root.right])


    def rob(self, root: TreeNode) -> int:
        # 思路：
        # 1）对于父节点， 最优解来自两个状态
        #    一个是选择父节点，则不能选择左右节点
        #    一个是不选择父节点，则问题转化为子问题，是否选择左右节点
        # 2） 状态转移函数：max(i_dict[root], non_dict[root])
        #     i_dict存放选择父节点的最优解结果， non_dict存放不选择父节点的最优解的结果
        
        # 设置hash map，字典中存放的是节点的对象
        i_list = {}             # 存放选择父节点的最优解的结果
        non_list = {}           # 存放不选择父节点的最优解的结果

        # 设置默认值
        i_list.setdefault(None, 0)
        non_list.setdefault(None, 0)

        self.dfs(root, i_list, non_list)

        # 选择父节点的最优解
        # 不选择父节点的最优解
        # 得出最终的最优解
        maxNum = max(i_list[root], non_list[root])

        return maxNum

        