from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 定义字典存放list中每个元素的个数
        dic = {}

        for i in nums:
            if i in dic:            # 如果元素i在字典中，则加一
                dic[i] = dic[i] + 1
            else:                   # 如果元素i不在字典中
                dic[i] = 1

            if dic[i] > int(len(nums) / 2):     # 如果元素i是多数元素，则返回
                return i 
            else:
                pass