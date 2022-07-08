'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 方法1：使用python自带的库
        # return list(itertools.permutations(nums))

        # 方法2：回溯法
        ans = []

        def backtrack(nums, temp):
            if nums == []:
                ans.append(temp)
                return 
            else:
                length = len(nums)
                for i in range(length):
                    new_nums = nums[:i] + nums[i+1:]
                    new_temp = temp[:] + [nums[i]]
                    backtrack(new_nums, new_temp)

        backtrack(nums, [])
        return ans 
