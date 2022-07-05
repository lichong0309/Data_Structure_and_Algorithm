'''
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
     
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

提示：
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅有小写英文字母组成
wordDict 中的所有字符串 互不相同
'''

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # 思路：当substring[i:j]在wordDict，同时substring s[:i]也在wordDict
        #      则sub string s[:j]在wordDict存在单词可以组成substring
        length = len(s)

        # dp表示 前i个字符串(不包括第i个字符) 在 wordDict的状态，
        # Fasle: 表示不在字符串中， True:表示在字符串中
        dp = [False] * (length+1)
        dp[0] = True

        # 遍历字符串，左起始点的索引
        for i in range(length):
            # 取字符串的长短，右终止点的索引
            for j in range(i+1, length+1):
                substring = s[i:j]
                if dp[i] == True and substring in wordDict:
                    dp[j] = True
        
        return dp[-1]




