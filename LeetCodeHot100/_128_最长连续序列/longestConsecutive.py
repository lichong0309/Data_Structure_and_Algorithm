'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0 
        
        dic = {}            # 存放字典，key为数组的元素，value为该元素已经发现的最长序列

        max_length = 0
        for num in nums:
            # 如果元素不在字典中
            if num not in dic:
                left = dic.get(num-1, 0)            # 获得该元素连续序列最左边的值，不存在则为0
                right = dic.get(num+1, 0)           # 获得该元素连续序列最右边的值，不存在则为0
                length= left + 1 + right            # 得到连续序列的长度

                if length > max_length:
                    max_length = length
                else:
                    pass
                
                # 更新元素的最长序列的值
                dic[num] = length
                # 更新连续序列最左边的值
                dic[num - left] = length
                # 更新连续序列最右边的值
                dic[num + right] = length

            # 如果已经在字典中
            else:
                pass


        ans = max_length
        return ans
