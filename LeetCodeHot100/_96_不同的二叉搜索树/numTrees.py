'''
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
输入：n = 3
输出：5


示例 2：
输入：n = 1
输出：1
 

提示：

1 <= n <= 19

'''
class Solution:
    def numTrees(self, n: int) -> int:
        # 递归：超时
        if n == 0 or n == 1:
            return 1
        else:
            sum = 0 
            for i in range(n+1):
                sum = sum + self.numTrees(i-1) * self.numTrees(n-i)
            return sum 

        # # 动态规划：
        # G = [0] * (n+1)
        # G[0], G[1] = 1, 1
        # # 计算：节点数量从2到n个，不同节点数量能组成的搜索二叉树的个数,保存在数组G中
        # # 最终返回G[n]即为需要的结果
        # for i in range(2, n+1):
        #     # 当有i个节点时，能组成的搜索二叉树的个数取决与左右节点的个数
        #     # 根节点j的取值为1到i，则左子树的个数为j-1, 右子树的个数为i-j
        #     for j in range(1, i+1):
        #         # 右子树能组成的搜索二叉树的个数 * 左子树组成的搜索二叉树的个数
        #         G[i] += G[i-j] * G[j-1]
        # return G[n]