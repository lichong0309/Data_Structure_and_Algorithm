'''
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"
 

提示：
1 <= s.length <= 1000
s 仅由数字和英文字母组成
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力方法
        # 时间复杂度 O(n^3) ： 超时

        # length = len(s)

        # subList = []
        # for i in range(length):
        #     for j in range(i, length):

        #         sbustring = s[i:j+1]                # 得到子字符串
        #         reversedstring = sbustring[::-1]    # 反转字符串

        #         if sbustring == reversedstring:
        #             l = len(sbustring)
        #             tup = (l, sbustring)        # 将回文字符串的长度和字符串存放到tuple中
        #             subList.append(tup)
        #         else:
        #             pass

        # # 排序 找到长度最大的回文字符串，降序排序
        # sortedList = sorted(subList, key=lambda x: x[0], reverse=True)

        # return sortedList[0][1]


        # 使用动态规划
        # 思路：如果s[i:j]（不包含j）是回文sub string， 则如果s[i-1] = s[j], 则s[i-1:j+1]也为回文sub string
        length = len(s)
        if length < 2:
            return s 

        else:
            # 例子 s="abaca", output="aba"
            # 创建一个 n*n 二维数组，存放从sub string s[i:j]是否是回文的
            # 初始化为：
            '''
                a  b  a  c  a
            a   1
            b      1
            a         1  
            c            1  
            a                1
            '''
            dp = [[False]*length for _ in range(length)]
            
            for i in range(length):
                dp[i][i] = True
            
            # 更新dp的表
            maxlen = 1          # 初始化最长的字符串个数
            begin = 0           # 初始化最长回文字符串的起始点为0

            # 从长度为2开始遍历字符串
            for L in range(2, length+1):
                # 得到字符串左边的起始位置
                for i in range(0, length-L+1):
                    
                    # 确定右边界
                    j = L + i -1

                    # 如果s[j]不等于s[j],则sub string[i,j+1]肯定不是回文字符串
                    # 比如s[a:b](包括b)
                    if s[j] != s[i]:
                        dp[i][j] = False

                    # 如果s[i]等于s[j]
                    else:

                        # 如果i和j之间的距离小于3，则在s[i]=s[j]的情况下，sub string s[i:j]肯定为回文字符串，
                        # 例如s[a:a]（包括a）,第一个a到第二个a
                        if j - i < 3:
                            dp[i][j] = True
                        
                        # 如果i和j之间的距离大于3
                        # 则需要判断他们之间的sub string是否为回文字符串
                        # 例如第一个a到最后一个a，需要判断b到c是否为回文字符串
                        else:
                            dp[i][j] = dp[i+1][j-1]

                    if dp[i][j] == True and (j-i+1) > maxlen:
                        begin = i 
                        maxlen = j - i +1
                        print(begin, maxlen)
                        
        print(begin, maxlen)
        return s[begin:begin+maxlen]
                                   



