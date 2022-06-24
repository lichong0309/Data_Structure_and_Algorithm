from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        else:
            nums.sort()
            ans = []

            for i in range(len(nums)):
                # 防止nums中的重复元素
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    left = i + 1        # 初始化left
                    right = len(nums)-1   # 初始化right

                    while left < right:
                        count = nums[i] + nums[left] + nums[right]
                        if count == 0:
                            ans.append([nums[i], nums[left], nums[right]])
                            # 当三个数之和已经为0，则需要移动两个位置，才有可能产生下一个三数之和为0的情况
                            left = left + 1
                            right = right - 1

                            # 找到下一个和left与right的值都不相同的位置，作为下次判断的left和right的起始点
                            while nums[left] == nums[left-1] and left < right:
                                left = left + 1 
                            while nums[right] == nums[right+1] and left < right:
                                right = right - 1 
                                
                        elif count < 0 :
                            # 这种情况需要left往后移动才能产生三数之和为0的情况
                            left = left + 1 

                        else:
                            # count > 0:
                            # 这种情况西药right往后移动才能产生三数之和为0的情况
                            right = right - 1
        return ans 
