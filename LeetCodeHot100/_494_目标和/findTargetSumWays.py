
'''
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
 

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''

from typing import List
class Solution:
    # 回溯法， 记忆化存储
    def help(self, nums, target, index, _sum, cache):
        # 回溯法， 记忆化搜索
        if (index, _sum) in cache:
            return cache[(index, _sum)]

        if index == len(nums):
            if _sum == target:
                cache[(index, _sum)] = 1
                return 1
            else:
                cache[(index, _sum)] = 0
                return 0
        else:
            left_ans = self.help(nums, target, index+1, _sum+nums[index], cache)
            right_ans = self.help(nums, target, index+1, _sum-nums[index], cache)
            cache[(index, _sum)] = left_ans + right_ans
        return left_ans + right_ans

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        ans = self.help(nums, target, 0, 0, cache)
        return ans 

