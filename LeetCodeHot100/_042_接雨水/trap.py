'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
 

提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 整体思路： 对于第i个柱子，能增加的水量为
        # i_left_max = max(height[:i+1]), i_right_max = max(height[i:])
        # water_amount = min(i_left_max, i_right_max) - height[i]

        # 1. 找到最高点
        # 2. 从左向最高点遍历
        # 3. 从右向最高点遍历
        length = len(height)
        if length == 1:
            return 0 
        
        # 寻找list中所有元素的最高点：
        maxNum = max(height)
        maxNumIndex = height.index(maxNum)
        print(maxNum, maxNumIndex)

        ans = 0 

        # 左半部分
        # 从左向最高点遍历，并记录 i元素 左边的 最大值
        i_left_max = height[0]
        for i in range(maxNumIndex):
            # 如果i元素的值 大于 左边的最大值，则对于i柱子，不能增加存储水的量
            if height[i] > i_left_max:
                i_left_max = height[i]
            else:
                water_amount = i_left_max - height[i]
                ans = ans + water_amount
        
        # 右半部分
        # 从右向最高点遍历，并记录j元素 右边的 最大值
        j_right_max = height[-1]
        for i in range(length-1, maxNumIndex, -1):
            # 如果j元素的值 大于 右边的最大值，则对于j柱子，不能增加存储水的量
            if height[i] > j_right_max:
                j_right_max = height[i]
            else:
                water_amount = j_right_max - height[i]
                ans = ans + water_amount
        
        return ans 

        
