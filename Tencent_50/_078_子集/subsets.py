from typing import List 
import copy

class Solution:
    def backtrack(self, nums, index, setList, ans):
        """_summary_

        Args:
            nums (List[int]): 数组，能够通过index找到对于的元素
            index (int): 找到nums中对于的元素
            setList (List[int]): 存放单个结果
            ans (List[int]): 存放最终的结果
        """
        length = len(nums)
        if index >= length:
            ans.append(setList)
        else:
            # 浅拷贝，也可以用用切片
            # setList_left = copy.copy(setList)
            # 注意：在python中 切片 明显比 浅拷贝 慢的很多
            setList_left = setList[:]
            setList_left.append(nums[index])
            setList_right = copy.copy(setList)
            self.backtrack(nums, index+1, setList_right, ans)
            self.backtrack(nums, index+1, setList_left, ans)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        setList = []
        self.backtrack(nums, index=0, setList=[], ans=ans)
        return ans