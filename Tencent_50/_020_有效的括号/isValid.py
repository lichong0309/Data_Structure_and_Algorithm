'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 

示例 1：
输入：s = "()"
输出：true


示例 2：
输入：s = "()[]{}"
输出：true


示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
 

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成


'''


class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈来存储 左括号，遇到右括号时 则出栈，判断是否对应
        stack = []          # 初始化栈

        for symbol in s:
            # 如果是左括号则入栈
            if symbol == '(' or symbol == '[' or symbol == '{':
                stack.append(symbol)        # 入栈

            # 如果是右括号，则出栈，判断是否对应
            else:
                # 如果栈为空，则返回False
                if stack == []:
                    return False
                
                else:
                    # 出栈
                    temp = stack.pop(-1)  
                    
                    #判断是否对应       
                    if temp == '(' and symbol == ')':
                        pass
                    elif temp == '[' and symbol == ']':
                        pass
                    elif temp == '{' and symbol == '}':
                        pass 

                    # 如果不对应，则返回False
                    else:
                        return False
        
        # 如果循环过后栈不为空，则返回False
        if len(stack) != 0:
            return False
        else:
            return True