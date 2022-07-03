'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [5,4,-1,7,8]
输出：23

提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
'''

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 遍历数组，时间复杂度 O(n)， n为nums的长度
        length = len(nums)

        dp = [0] * length
        
        dp[0] = nums[0]
        
        for i in range(1, length):
            # 如果dp[i-1]>0, 则加上之前的 和(即dp[i-1]) 可能出现最大和
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + nums[i]

            # 如果dp[i-1]<0， 则加上之前的 和(即dp[i-1]) 不可能比dp[i]大，所以dp[i]=nums[i]
            else:
                dp[i] = nums[i]

        ans = max(dp)
        return ans
            

