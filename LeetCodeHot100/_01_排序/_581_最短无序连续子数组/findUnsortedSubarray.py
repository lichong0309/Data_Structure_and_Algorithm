'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。


示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0

示例 3：
输入：nums = [1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 对nums进行升序排序,后续比较
        n = sorted(nums, reverse=False)
        length = len(nums)         # nums长度
        count = 0                  # 计数
        left = 0                   # 左指针
        right = length - 1         # 右指针
        
        # 左指针遍历
        while left <= right and left < length and nums[left]==n[left]:
            count = count + 1 
            left = left + 1

        # 右指针遍历
        while left < right and right > 0 and nums[right]==n[right]:
            count = count + 1
            right = right - 1 
            
        count = length - count 
        return count 


        

            