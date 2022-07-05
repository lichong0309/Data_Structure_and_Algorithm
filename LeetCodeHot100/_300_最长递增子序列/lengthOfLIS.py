'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
 
提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 
进阶：
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]结尾的，最长的严格递增子序列的长度，初始化为1
        length = len(nums)

        dp = [1]* length

        # 遍历nums
        for i in range(length):
            # 从0 到i-1遍历，寻找以nums[i]结尾的最长严格递增子序列
            # 对于前i个nums中的元素来说，一定存在一个严格递增的子序列，且以nums[n]结尾，有n<i， j在遍历的过程中会扫描到n。
            # 存在两种情况：
            # 1) 如果nums[n] < nums[i], 则会增加目前最长递增子序列的长度
            # 2) 如果nums[n] >= nums[j], 则另在dp[i]中记录以nums[i]结尾的最长递增子序列的长度，且对之前的递增子序列没有影响，并且可能在之后的遍历中产生更长的递增子序列
            for j in range(i):
                if nums[i] > nums[j]:
                    # dp[i]要么来自于初始化
                    # 要么来自于nums[:i] sub list对于的dp[j], j < i
                    extend_dp = dp[j] + 1       
                    dp[i] = max(extend_dp, dp[i])
        
        ans = max(dp)
        return ans 