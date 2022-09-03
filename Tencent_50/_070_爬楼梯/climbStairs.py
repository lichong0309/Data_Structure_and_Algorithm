'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 
提示：
1 <= n <= 45
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        # 存在关系 dp[i] = dp[i-1] + dp[i-2]

        if n == 1:
            return 1

        elif n == 2:
            return 2

        else:
            # 初始化dp数组，从0到n，即n+1个元素
            dp = [0] * (n+1)            

            dp[1], dp[2] = 1, 2

            # 从3到索引为n
            for i in range(3, n+1):
                dp[i] = dp[i-1]  + dp[i-2] 

            # 返回dp[n]为最终结果
            return dp[n]