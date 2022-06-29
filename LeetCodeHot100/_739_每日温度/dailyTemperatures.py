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


from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # 第一种方法， 超时
        # ans = []
        # for i in range(len(temperatures)):
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[i] < temperatures[j]:
        #             flag = 1
        #             break 
        #         else:
        #             j = j + 1

        #     if j < len(temperatures):
        #         ans.append(j-i)
        #     else:
        #         ans.append(0)
                
        # return ans

        # 第二种方法： 单调栈
        ans = [0] * len(temperatures)       # 初始化和temperatrus一样的list，元素为0
        # 创建栈,栈中保存索引index
        # 如果索引存在栈中，说明该索引在temperatures中的值未找到第一个比他大的元素
        # 有两种情况，一种是比他大的元素还没有出现，另一种情况是没有比他大的元素
        stack = []                          

        # 循环所有元素
        for i in range(len(temperatures)):
            # 如果是第一个元素，则直接压栈
            if i ==  0:
                stack.append(i)
            
            else:
                # 循环条件：
                # 1. 当stack不为空，说明还有元素没有找到第一个比他大的元素
                # 2. 当新的元素比stack中栈顶元素大时，则需要退出栈顶元素
                while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                    # 退栈
                    discard = stack.pop(-1)
                    ans[discard] = i - discard
                
                # 将i压栈
                stack.append(i)
        
        return ans 

