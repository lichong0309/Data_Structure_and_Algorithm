'''
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 
提示：
1 <= s.length <= 1000
s 由小写英文字母组成

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 使用动态规划
        length = len(s)
        
        dp = [[False]*length for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

        count = length
        # sub string的长度可以是 1 到 length
        for i in range(2, length+1):
            # 左起始点
            for j in range(0, length-i+1):
                # 右终结点
                m = j + i - 1

                # 如果终结点 和 起始点 不相同， 则该sub string 肯定不是回文字符串
                if s[m] != s[j]:
                    dp[j][m] = False
                # 如果终结点 和 起始点 相同
                else:
                    # 如果 终结点 和 起始点 的距离小于3，则sub string为回文字符串
                    if i <= 3:
                        dp[j][m] = True
                        count = count + 1
                    
                    else:
                        dp[j][m] = dp[j+1][m-1]
                        if dp[j][m] == True:
                            count = count + 1
                        else:
                            pass
            
        return count        