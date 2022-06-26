'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        # 1. 对输入的intervals进行排序
        intervals.sort()
        
        # 2. 合并区间
        length = len(intervals)     # list的长度
        i = 0                       # 初始化第一个区间的起始点

        
        while i < length:
            start = intervals[i][0]         # 初始化不覆盖区间的start为intervals[i][0]
            end = intervals[i][1]           # 初始化不覆盖区间的end为intervals[i][1]
            
            # 开始寻找不覆盖区间的end
            j = i + 1                       
            # 如果第j个元素的start值小于第i个元素的end的值，则出现覆盖区间
            while j < length and intervals[j][0] <= end:
                if intervals[j][1] > end:
                    end = intervals[j][1]    # 更新不覆盖区间的end
                j = j + 1
                
            ans.append([start, end])

            i = j               # 找到下一个区间的起始点

        return ans
