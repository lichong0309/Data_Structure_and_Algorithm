'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]
 

提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

'''

from typing import List
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
            
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        ans = []
        self.backtrack(digits, dic, 0, '', ans)
        return ans 
    
    def backtrack(self, digits, dic, index, path, ans):
        """很标准的回溯算法

        Args:
            digits (str): 输入的数字
            dic (dict): 寻找数字对应的字母数组
            index (int): digits的元素索引 
            path (List[int]): 存放可能的结果
            ans (List[int]): 存放所有符合要求的结果
        """
        if index == len(digits):
            ans.append(path)
            return 
        else:
            charList = dic[digits[index]]
            for item in charList:
                self.backtrack(digits, dic, index+1, path+item, ans)
        
    
                