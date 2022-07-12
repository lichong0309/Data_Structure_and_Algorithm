'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]


示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]


示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''


from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找到左边界和右边界
        left_board = self.get_left(nums, target)            # 左边界
        right_board = self.get_right(nums, target)          # 右边界
        return [left_board, right_board]
    
    # 找左边界
    def get_left(self, nums, target):
        length = len(nums)
        left = 0
        right = length - 1
        left_board = -1                 # 初始化左边界为-1
        
        while left <= right:
            mid = (left + right) // 2

            # 如果nums中有target，则更新left_board    
            if nums[mid] == target:
                left_board = mid
            
            # 因为是找左边界，所以当nums[mid] == target时，只需要在左部分左二分法即可，不需要在右部分左二分法，丢弃右部分
            
            # 如果在左部分,检查左部分是否还存在target，如果有，则更新left_board
            if target <= nums[mid]:
                right = mid - 1 
            
            # 如果当target不可能存在左部分，则在右部分做二分法
            elif target > nums[mid]:
                left = mid + 1
        
        return left_board


    # 找右边界
    def get_right(self, nums, target):
        length = len(nums)
        left = 0 
        right = length - 1
        right_board = -1

        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] == target:
                right_board = mid


            # 因为是找右边界，所以当nums[mid] == target时，只需要在右部分做二分法，不需要在左部分做二分法，丢弃左部分

            # 如果在右部分，检查右部分是否还存在target， 如果有，则更新right_board
            if nums[mid] <= target:
                left = mid + 1
        
            # 如果不可能在右部分，则在左部分做二分法
            elif nums[mid] > target:
                right = mid - 1

        return right_board