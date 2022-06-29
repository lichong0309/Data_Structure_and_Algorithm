
'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 
示例 2：
输入：nums = [1], k = 1
输出：[1]
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

'''


from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 第一种方法：超时
        ans = []
        queue = []

        # 第一个窗口
        queue = nums[:k]
        maxNum = max(queue)
        ans.append(maxNum)

        for i in range(k, len(nums)):
            # 出队列
            discard = queue.pop(0)
            # 入队列
            queue.append(nums[i])
            # 如果出队列的元素是最大的元素，则需要重新比较
            if maxNum == discard:
                maxNum = max(queue)
            # 如果出队列的元素不是最大的元素，则只需要比较最大元素和新入队列的元素
            else:
                maxNum = max(maxNum, nums[i])
            # 加入ans中
            ans.append(maxNum)
        
        return ans 
        

        # # 第二种方法： 最大堆
        # # 创建第一个窗口的最大堆
        # ans = []
        # h = [(-nums[i], i) for i in range(k)]
        # heapq.heapify(h)
        # ans.append(-h[0][0])

        # # 移动窗口，并且维护最大堆特性
        # for i in range(k, len(nums)):
        #     # 添加新的元素到最大堆中
        #     heapq.heappush(h, (-nums[i], i))
        #     # 退出不在当前窗口的元素
        #     while h[0][1] <= (i-k):
        #         heapq.heappop(h)
        #     ans.append(-h[0][0])

        # return ans 


        # 第三种方法： 队列
        ans = []            # 存放结果
        queue = []          # 队列
        
        # 创建第一个窗口的队列
        for i in range(k):
            # 如果当前的元素比队列的元素大，则只需要存储当前的元素即可
            # 但是如果当前的元素比队列的元素小，则需要存储，因为当前元素可能在下个窗口中为最大的元素
            while queue != [] and nums[i] >= nums[queue[-1]]:
                queue.pop(-1)
            # 添加 1）当前窗口的最大值的索引，2）当前窗口最大值后面的单调递减元素的索引
            queue.append(i)
        # 存储第一个窗口的最大值
        ans.append(nums[queue[0]])


        # 对后面的窗口进行处理
        for i in range(k, len(nums)):
            # 同第一个元素，存储1）当前窗口的最大值 2） 当前窗口最大值后面的单调递减元素的索引
            while queue != [] and nums[i] >= nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i)

            # 删除不在当前窗口的队列中的索引
            while queue[0] <= (i-k):
                queue.pop(0)
            
            # 队列中的第一个元素即是当前窗口的最大值的索引
            ans.append(nums[queue[0]])

        return ans


        

                
