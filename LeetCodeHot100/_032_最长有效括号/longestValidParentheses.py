'''
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 使用栈，栈中存放 元组 tuple(symbol:char, index:int)
        # 参考 第20题，有效的括号
        stack = []
        # temp = []
        length = len(s)
        if length == 0:
            return 0
    
        for i, item in enumerate(s):
            # 如果 为 左括号， 则压栈
            if item == "(":
                stack.append((item,i))
            # 如果 为 右括号
            else:
                # 如果栈为空
                if stack == []:
                    stack.append((item, i))
                # 如果 栈不为空
                else:
                    # 如果 栈顶 的元素为 左括号，则退栈
                    if stack[-1][0] == "(":
                        stack.pop(-1)
                    # 如果栈顶 的元素为 右括号， 则将新来的符号 入栈
                    else:
                        stack.append((item, i))

        stack_list = []
        for item in stack:
            stack_list.append(item[1])

        # 插入边界，便于操作
        stack_list.insert(0, -1)
        stack_list.append(length)

        len_stack = len(stack_list)
        # dp[i]表示在stack_list中的第i个元素前面 第一个连续有效的的括号的长度
        dp = [0] * (len_stack)

        for i in range(1, len_stack):
            dp[i] = stack_list[i] - stack_list[i-1] - 1
        ans = max(dp)
        return ans 

