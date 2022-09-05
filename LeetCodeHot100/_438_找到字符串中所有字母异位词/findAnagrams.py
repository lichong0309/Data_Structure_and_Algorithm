'''
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

提示:

1 <= s.length, p.length <= 3 * 104
s和p仅包含小写字母

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        # 思路： 判断滑动窗口的每个字母的数量与子串的字母数量是否相等，来判断滑动窗口中的字符串是否为淄川的异位词
        ans = []

        s_len = len(s)
        p_len = len(p)
        
        if s_len < p_len:
            return ans 

        p_count = [0] * 26
        s_count = [0] * 26

        # s字符串0号位置为特殊位置，拿出来单独处理
        for i in range(p_len):
            p_location = ord(p[i]) - ord("a")
            p_count[p_location] += 1

            s_location = ord(s[i]) - ord('a')
            s_count[s_location] += 1

        # 如果s_count == p_count
        if s_count == p_count:
            ans.append(0)
        else:
            pass

        # s字符串0号位置之外的其他位置
        # 当前窗口的s_count为：减去前一个窗口的最左边位置的值，加上新加入的位置作为当前窗口最右边的位置，中间位置不需要修改，减少了运行的时间
        for i in range(0, (s_len - p_len)):
            left_location = ord(s[i]) - ord('a')        # 上一个窗口的最左边的位置
            s_count[left_location] -= 1                 # 减去上一个窗口最左边的位置
            right_location = ord(s[i+p_len]) - ord('a') # 当前窗口最右边的位置
            s_count[right_location] += 1                # 加上当前窗口新加入的元素

            left_windows = i + 1            # 当前窗口的左起始位置
            if s_count == p_count:
                ans.append(left_windows)
            else:
                pass
        return ans
        