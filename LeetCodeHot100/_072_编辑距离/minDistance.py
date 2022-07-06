'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
 
提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        
        '''
        创建二维数组dp, dp[i][j]表示word1中前i个字符最少需要多少步变换成word2中的前j个字符
        example: “sea”, "eat"
        
            *   e   a   t    
        *   0   1   2   1
        s   1   1   2   1 
        e   2   1   2   2 
        t   0   1   1   2
        
        '''
        dp = [[0]*(length2+1) for _ in range(length1+1)]

        # # 初始化某些值
        # if word1[0] != word2[0]:
        #     dp[0][0] = 1
        # 初始化第一行数据
        for j in range(1, length2+1):
            dp[0][j] = dp[0][j-1] + 1
        # 初始化第一列的数据
        for i in range(1, length1+1):
            dp[i][0] = dp[i-1][0] + 1 

        for i in range(1, length1+1):
            for j in range(1, length2+1):
                # 存在三个状态转移的方向
                # 1. 斜对角线 diagonal
                if word1[i-1] == word2[j-1]:
                    diagonal = dp[i-1][j-1]
                else:
                    diagonal = dp[i-1][j-1] + 1
                # 2. 上方转移的状态
                up = dp[i-1][j] + 1
                # 3. 左边转移的状态
                left = dp[i][j-1] + 1

                dp[i][j] = min(diagonal, up, left)
        
        return dp[length1][length2]



'''
1. 状态转移从 对角线 来
问题1：如果 word1[0..i-1] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要几步呢？

答: 先使用 k 步，把 word1[0..i-1] 变换到 word2[0..j-1]，消耗 k 步。再把 word1[i] 改成 word2[j]，就行了。
    如果 word1[i] == word2[j]，什么也不用做，一共消耗 k 步，否则需要修改，一共消耗 k + 1 步。

2.状态转移从 上方 来
问题2：如果 word1[0..i-1] 到 word2[0..j] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？

答: 先经过 k 步，把 word1[0..i-1] 变换到 word2[0..j]，消耗掉 k 步，
    再把 word1[i] 删除，这样，word1[0..i] 就完全变成了 word2[0..j] 了。一共 k + 1 步。

3. 状态转移从 左遍 来
问题3：如果 word1[0..i] 到 word2[0..j-1] 的变换需要消耗 k 步，那 word1[0..i] 到 word2[0..j] 的变换需要消耗几步呢？

答：先经过 k 步，把 word1[0..i] 变换成 word2[0..j-1]，消耗掉 k 步，
    接下来，再插入一个字符 word2[j], word1[0..i] 就完全变成了 word2[0..j] 了。
'''