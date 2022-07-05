'''
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]
 

提示：
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。
'''


from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 题目要求：时间复杂度O(n)
        # 思路：将nums中的元素作为下标，对下标对应的nums的元素取负数
        #      最终为正值对应的索引，即为从未出现的数字
        length = len(nums)
        for i in range(length):
            # 得到索引
            index = abs(nums[i])            # 取绝对值：防止前面取负数的时候nums[i]被篡改
            nums[index-1] = -abs(nums[index-1])     # 取绝对值：防止nums中有重复的数字，多次修改nums的同一个元素，使得最终取址不正确
        # print(nums)
        
        ans = []
        for i, val in enumerate(nums):
            if val > 0:
                ans.append(i+1)         # 注意索引需要加1

        return ans