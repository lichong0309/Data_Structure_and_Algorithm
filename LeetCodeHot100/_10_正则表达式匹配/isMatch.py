'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

 
示例 1：

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
 

提示：

1 <= s.length <= 20
1 <= p.length <= 30
s 只包含从 a-z 的小写字母。
p 只包含从 a-z 的小写字母，以及字符 . 和 *。
保证每次出现字符 * 时，前面都匹配到有效的字符
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)
        dp = [[False]*(plen+1) for _ in range(slen+1)]

        # 初始化
        dp[0][0] = True 
        for j in range(1, plen+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]       # 因为在dp前面补了一行和一列，所以dp的索引和s,p的索引不对应，需要是j-2
        

        for i in range(1, slen+1):
            for j in range(1, plen+1):
                # 如果当前s的元素和p的元素相同，则dp[i][j]的状态来自于 右上角
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                
                # 如果当前p的元素为“*”
                elif p[j-1] == "*":
                    # 如果当前的s的元素和“*”之前的元素相同，
                    # 该“*”可以不使用，则dp[i][j]的状态来自于 “*”之前的状态的转移，即dp[i][j-2]
                    # 该“*”使用到，则dp[i][j]的状态来自于 当前“*”的拓展的字符，即dp[i-1][j]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]

                    # 如果当前的s的元素和“*”之前的元素不相同
                    # 则该“*”不能使用，则dp[i][j]的状态来自于 “*”之前的状态的转移，即dp[i][j-2]
                    elif s[i-1] != p[j-2] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
         
        ans = dp[slen][plen]
        return ans 






        # 题目理解错误，但是该方法可以用在正则表达式完全匹配上
        # slen = len(s)
        # plen = len(p)

        # dp = [[False]*slen for _ in range(plen)]

        # if p[0] == "*":
        #     for j in range(slen):
        #         dp[0][j] = True 
        # elif p[0] == '.':
        #     dp[0][0] = True 
        # elif p[0] == s[0]:
        #     dp[0][0] = True 
        # else:
        #     return False
        
        # for i in range(1, plen):
        #     if p[i] == "*":
        #         # 状态转移来自于左边和上边
        #         dp[i][0] = dp[i-1][0] 
        #         for j in range(1, slen):
        #             dp[i][j] = dp[i][j-1] or dp[i-1][j]
            
        #     elif p[i] == ".":
        #         # 状态转移来自于 上边 和 斜对角
        #         for j in range(1, slen):
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-1]
        #     # 如果为字符
        #     else:
        #         for j in range(1, slen):
        #             dp[i][j] = (p[i]==s[j]) and (dp[i-1][j] or dp[i-1][j-1])

        # print(dp)
        # ans = dp[-1][-1]
        # return ans