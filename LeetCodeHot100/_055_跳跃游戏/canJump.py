'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

'''

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 如果能到达某个位置，则一定能到达该位置的前面的位置
        index_length = len(nums) - 1

        max_jump = nums[0]

        for i, item in enumerate(nums):
            # 如果i是前几步能到达的地方
            if i <= max_jump:
                # 得出i能到达的最远的地方
                max_jump_i = i + item 
                # 如果i能到达的最远的地方 超过了 前几步到达的地方，则更新能到达的最远的地方max_jump
                if max_jump_i > max_jump:
                    max_jump = max_jump_i
                else:
                    pass
                
                # 如果能到达的最远的地方 超过或者等于 最后一个位置
                # 则返回True
                if max_jump >= index_length:
                    return True 
                else:
                    pass
            else:
                pass
        # 最后如果不能到达 最后一个位置， 则返回False
        return False