'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
 

提示:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

进阶：你能尽量减少完成的操作次数吗？
'''

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 方法一：
        # count = nums.count(0)
        # for i in range(count):
        #     nums.remove(0)
        #     nums.append(0)

        # 方法二：
        # 设置两个指针
        # 最终 left指向第一个零元素
        # 从left到right均为零元素
        left, right = 0, 0 
        length = len(nums)
        for i in range(length):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                # 每遍历到一个非零元素，则left向右移动一位，最终指向第一个零元素
                left = left + 1
            right = right + 1 

