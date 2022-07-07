'''
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。


示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
 
提示：
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 0-1背包问题
        # 思路：从nums list中选择若干个元素，使得他们的和为所有元素的和的一半
        length = len(nums)
        nums_sum = sum(nums)

        # 如果nums的长度为1，或者所有元素的综合为奇数，则不可能存在分成两个元素和相同的数组的情况
        if length == 1 or (nums_sum % 2) != 0:
            return False 

        target = int(nums_sum // 2)

        # 创建二维数组，dp[i][j]表示前i个元素能否组成元素和为j的情况
        # 因为后面需要使用到j-nums[i]可能等于0的索引，所以在纵向上添加0的一行索引
        dp = [[False]*(target+1) for _ in range(length)]

        
        '''
        如果 dp = [[False]*(target+1) for _in range(length+1)]
        则不需要初始化第一行
        '''
        # 初始化第一行为True
        dp[0][0] = True
        # 如果nums第一个元素小于target
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # '''
        # 状态转移函数，两种情况
        # 1. dp[i][j] = dp[i-1][j]      nums[i] > j
        # 2. dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]      nums[j] < j
        # '''

        # 遍历nums中的所有元素
        for i in range(1, length):
            # 遍历横轴的所有元素
            for j in range(target+1):
                # 默认第一列的所有元素为True
                if j == 0:
                    dp[i][j] == True
                else:
                    if nums[i] > j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

        return dp[length-1][target]