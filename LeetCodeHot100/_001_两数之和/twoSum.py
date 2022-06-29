
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？


'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     remain = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == remain:
        #             return [i,j]
        #         else:
        #             pass

        # 使用字典
        # dic:{key, value}
        # key: 已经扫描的元素对应的remain = target - val 的值
        # value: 已经扫描的元素的索引
        # 例如：[2, 7, 11, 15] dic={7:1, 2:1, -3:2, -6:3}
        dic = {}
        for ind, val in enumerate(nums):
            # 如果正被扫描的元素在字典中，说明之前扫描的元素和当前元素符合要求
            # 则返回他们的索引
            if val in dic:
                return [dic[val], ind]
            
            # 如果当前扫描的元素不在字典中，则添加到字典中，供后面的元素判断
            else:
                remain = target - val 
                dic[remain] = ind


