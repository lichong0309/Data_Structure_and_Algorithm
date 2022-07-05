'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 方法一
        # # 返回字典 dic: dict{int:int}
        # # key为nums的元素，value为字符串中元素在nums中出现的次数
        # dic = collections.Counter(nums)

        # # 对字典进行value升序排序
        # sort_dic = sorted(dic.items(), key=lambda x:[x[1],x[0]])

        # return sort_dic[0][0]

        # 方法二，使用异或
        # 1. 相同的数异或为0    n^n=0
        # 2. 任何数与0以后，还为任何数  n^0=n
        ans = 0 
        for num in nums:
            ans = ans ^ num
        return ans 
            