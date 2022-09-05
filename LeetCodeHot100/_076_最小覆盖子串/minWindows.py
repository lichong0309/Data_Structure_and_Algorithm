'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

'''


from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""

        s_len = len(s)
        t_len = len(t)

        # 初始化两个字典，并设置默认值为0
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        # 初始化t_dic
        for i in range(t_len):
            t_dic[t[i]] += 1

        left, right = 0, 0
        count = 0 
        while right < s_len:
            
            # 更新s_dic的值
            s_dic[s[right]] += 1
            
            # 如果s【right】在s_dic中的值小于t_dic
            # 则说明s[right]元素是需要的
            # count表示计数已经找到的字符串中的字符
            if s_dic[s[right]] <= t_dic[s[right]]:
                count += 1
            else:
                pass
            
            # 缩小窗口
            # 1. 如果左边的元素不在字符串t中，则删除该元素，缩小窗口
            # 2. 如果左边的元素是多余的，则删除该元素，缩小窗口
            while left <= right and (t_dic[s[left]] == 0 or s_dic[s[left]] > t_dic[s[left]]):
                s_dic[s[left]] -= 1
                left += 1
            
            # 如果count==t_len，说明已经找到了所有字符串t中的字符
            if count == t_len:
                # 需要最小的符合要求的s的子串
                if ans == "" or (right - left + 1) < len(ans):
                    ans = s[left:right+1]                   # 截取子串
                else:
                    pass
            else:
                pass

            right += 1

        return ans
        


