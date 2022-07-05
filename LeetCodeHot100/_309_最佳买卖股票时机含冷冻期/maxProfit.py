'''
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
输入: prices = [1]
输出: 0

提示：
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0]*3 for _ in range(length)]

        # dp[i][0]：第i天结束持有股票的最大收益
        # dp[i][1]：第i天结束不持有股票，且在冷冻期的最大收益
        # dp[i][2]：第i天结束不持有股票，且不在冷冻期的最大收益

        dp[0][0] = -prices[0]

        for i in range(1, length):
            # 对于dp[i][0]
            # 1) 第i-1天持有股票：第i天不卖出
            # 2) 第i天买入： 第i-1未持有股票，且不在冷冻期
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            
            # 对于dp[i][1]
            # 1) 第i天卖出：第i天结束股票处在冷冻期, 且第i-1天持有股票
            dp[i][1] = prices[i] + dp[i-1][0]

            # 对于dp[i][2]: 当天未操作，且第i-1天 未持有股票
            # 1) 第i-1天未持有股票，且在冷冻期
            # 2) 第i-1天未持有股票，且不在冷冻期
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[length-1][1], dp[length-1][2])