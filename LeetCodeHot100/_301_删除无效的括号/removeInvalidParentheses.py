'''
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

示例 1：
输入：s = "()())()"
输出：["(())()","()()()"]

示例 2：
输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

示例 3：
输入：s = ")("
输出：[""]
 

提示：
1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号
'''

from typing import List
class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        left_remove, right_remove = self.get_remove_num(s)
        self.backtrack(s, 0, left_remove, right_remove, ans)
        return ans 

    def get_remove_num(self, s):
        # 得到对于字符串s需要删除的左括号和右括号的数量
        left_remove, right_remove = 0, 0 
        for c in s:
            if c == "(":
                left_remove = left_remove + 1
            elif c == ")":
                if left_remove > 0:
                    left_remove = left_remove - 1
                else:
                    right_remove = right_remove + 1
        return left_remove, right_remove

    def isValid(self, s):
        # 左括号需要永远 大于 或者等于 右括号
        # 否则 则不合法
        count = 0       # 记录 左括号的数量 - 右括号的数量
        for c in s:
            if c == "(":
                count = count + 1
            elif c == ")":
                count = count - 1 
                if count < 0:
                    return False
        return count == 0


    def backtrack(self,s, start, left_remove, right_remove, ans):

        if left_remove == 0 and right_remove == 0:
            if self.isValid(s) == True:
                ans.append(s)

        for i in range(start, len(s)):
            # 去重复
            if i > 0 and s[i] == s[i-1]:
                continue

            # 去除一个左括号
            if s[i] == "(" and left_remove > 0:
                new_s = s[:i] + s[i+1:]         # 删除s[i]
                self.backtrack(new_s, i, left_remove-1, right_remove, ans)

            # 去除一个右括号
            elif s[i] == ")" and right_remove > 0:
                new_s = s[:i] + s[i+1:]         # 删除s[i]
                self.backtrack(new_s, i, left_remove, right_remove-1, ans)


