'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4
 

提示：

1 <= heights.length <=105
0 <= heights[i] <= 104
'''

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 核心思想：
        # 对于索引i的元素，能围成的最大面积为：
        # max_area = left_area + right_area + heights【i】
        # left_area: 找到 左边 第一个比heights[i]小的元素
        # right_area: 找到 右边 第一个比heights[i]小的元素


        heights = [0] + heights + [0]
        length = len(heights)

        stack = []
        ans = 0 
        for i in range(length):
            # 入栈
            if stack == [] or heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                # 出栈
                while stack != [] and heights[i] < heights[stack[-1]]:
                    # 出栈
                    tmp = stack.pop()

                    # 左边 第一个最小值
                    left = stack[-1]
                    # 右边 第一个最小值
                    right = i
                    
                    area = heights[tmp] * (right - left - 1)

                    ans = max(area, ans)

                # 将新的值入栈
                stack.append(i)

        return ans 