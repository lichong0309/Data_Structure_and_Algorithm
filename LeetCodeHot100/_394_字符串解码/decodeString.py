'''
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]


示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
 

提示：

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

'''



class Solution:
    def decodeString(self, s: str) -> str:

        multi = 0 
        ans = ''
        stack = []

        for ch in s:
            
            # 当ch为数字时：
            if ch >= '0' and ch <= '9':
                multi = multi * 10 + int(ch)

            # 当ch为左括号
            # 入栈
            elif ch == '[':
                before_ans = ans 
                stack.append([before_ans, multi])
                ans = ''
                multi = 0            

            # 当ch为右括号
            # 出栈
            elif ch == ']':
                element = stack.pop(-1)
                before_ans = element[0]
                cur_multi = element[1]
                ans = before_ans + ans * cur_multi
            
            # 当ch为字符串
            else:
                ans = ans + ch

        return ans
                


            


                    


            
            