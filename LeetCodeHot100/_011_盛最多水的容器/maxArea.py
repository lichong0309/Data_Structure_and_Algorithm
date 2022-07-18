'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

 

示例 1：



输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
 

提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

'''


from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 如果向内移动短板，则min(h[i],h[j])可能变大，也可能变小，面积也可能变大，也可能变小
        # 如果向内移动长板，则min(h[i],h[j])一定要么变小，或者不变，所以面积一定变小或者不变
        # 所以思路：
        # 可以消除移动长板带来简化计算过程，因为移动长板不可能出现新的最大的值

        i = 0
        j = len(height) - 1

        ans = 0 

        while i < j:
            if height[i] < height[j]:
                amount = height[i] * (j-i) 
                ans = max(amount, ans)
                i = i + 1                       # 移动短板
            else:
                amount = height[j] * (j-i)
                ans = max(amount, ans)
                j = j - 1                       # 移动短板

        return ans 