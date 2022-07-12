'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104
'''


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 因为时间复杂度是O(logN)
        length = len(nums)

        left = 0
        right = length - 1

        while left <= right:

            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            # 如果mid左边是有序的
            # 则先判断是否target是否在左边，如果不在则将二分查找转移到右边
            if nums[left] <= nums[mid]:
                # 如果target落在左边：
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 如果target没有落在mid左边，则肯定在mid的右边
                else:
                    left = mid + 1          # 将left移动到mid的右边
            
            # 如果mid右边是有序的
            # 则先判断是否target是否在右边，如果不在则将二分查找转移到左边
            else:
                # 如果target在mid的右边:
                if nums[mid] < target  <= nums[right]:
                    left = mid + 1
                # 如果target在mid的左边
                else:
                    right = mid - 1          # 将right移动到mid的左边

        return -1

