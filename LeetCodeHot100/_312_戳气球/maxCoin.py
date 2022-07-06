'''
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10
 

提示：
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100

'''
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # 动态规划
        l = len(nums)
        # 在头部和末尾添加1
        nums.insert(0, 1)
        nums.insert(l+1, 1)            

        # 新的长度
        length = len(nums)

        # 创建二维数组
        # dp[i][j] 表示 开区间(i,j)中， 能获得的硬币的最大数量
        dp = [[0]*(length) for _ in range(length)]

        # 遍历不同的区间长度
        for n in range(2, length+1):
            # 开区间 的 左起始点
            for i in range(0, length-n+1):
                
                # 开区间 的 右终点
                j = i + n - 1

                # k在 开区间 中取值，作为最后一个被戳爆的气球
                maxNum_in_i_j = 0           # 初始化开区间（i，j）的最大硬币数量为0 
                for k in range(i+1, j):
                    left = dp[i][k]         # 开区间 （i，k）的最大硬币数量
                    right = dp[k][j]        # 开区间 （k,j）的最大硬币数量
                    coin_k = nums[i] * nums[k] * nums[j]    # 开区间（i，j）只剩下k时能获取的硬币数量   
                    coin_i_j = left + right + coin_k
                    # 得到开区间（i，j）的最大硬币数量
                    if coin_i_j > maxNum_in_i_j:
                        maxNum_in_i_j = coin_i_j
                        
                # 开区间（i，j）的最大硬币数量
                dp[i][j] = maxNum_in_i_j
        
        return dp[0][length-1]






