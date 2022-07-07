'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''


from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        length = len(coins)

        # 如果dp = [[float("inf")]*(amount) for _ in range(length)],则需要初始化dp中的第一行数据
        # 创建二维数组， 分别设置了辅助列和辅助行，不需要初始化
        # 初始化为最坏的情况
        dp = [[float("inf")]*(amount+1) for _ in range(length+1)]
        dp[0][0] = 0            # 设置dp中确定的值

        for i in range(1, length+1):
            for j in range(amount+1):
                # 如果该硬币的面值 大于 总的金额，则该硬币对总的金额没有影响
                # 则状态转移来自于 上一个硬币
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                # 如果该硬币的面值 小于 总的金额，则该硬币 可能 对 总的金额 有影响
                # 则状态转移来自于 上个硬币，和该硬币
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
        
        if dp[length][amount] != float('inf'):
            return dp[length][amount]
        else:
            return -1
