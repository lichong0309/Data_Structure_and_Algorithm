class Solution:
    def largestRectangleArea(self, heights) -> int:
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

nums = [2,1,5,6,2,3]

s = Solution()
ans = s.largestRectangleArea(nums)
print(ans)