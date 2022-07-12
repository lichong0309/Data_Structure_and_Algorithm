'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 

 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 方法1，暴力法，使用合并之后找到中位数
        n1 = len(nums1)
        n2 = len(nums2)
        newList = []
        p1 = 0 
        p2 = 0 
        while p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                newList.append(nums1[p1])
                p1 = p1 + 1
            else:
                newList.append(nums2[p2])
                p2 = p2 + 1
        
        if p1 != n1:
            newList = newList + nums1[p1:]
        else:
            newList = newList + nums2[p2:]
        
        n = (n1+n2) // 2
        # 偶数
        if (n1+n2) % 2 == 0:
            ans = (newList[n-1] + newList[n]) / 2
        # 基数
        else:
            ans = newList[n]

        return ans 



        