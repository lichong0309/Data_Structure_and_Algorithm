'''
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

示例 1：
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。

示例 2：
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：
输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都 互不相同
1 <= target <= 500
'''


from typing import List
class Solution:
    def backtrack(self, candidates, target, begin, path, ans):
        """_summary_

        Args:
            candidates (List[int]): 原始数组
            target (int): 目标值
            begin (int): 每次遍历的开始的索引，避免和前面的搜索重复，则遍历在candidates中begin索引之后的元素
            path (_type_): 记录符合要求的组合
            ans (_type_): 记录所有符合要求的组合
        """
        if target == 0:
            ans.append(path)
            return 
        else:
            for i in range(begin, len(candidates)):
                t = target - candidates[i]
                # 因为已经对candidates做了排序处理
                # 如果对与target减去小的值的结果小于0，则对于循环后面更大的值，则会更小于0，则不需要循环，break退出
                if t < 0:
                    break
                else:
                    new_path = path + [candidates[i]]           # 新的路径
                    self.backtrack(candidates, t, i, new_path, ans)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        self.backtrack(candidates, target, 0, path, ans)
        return ans 