class Solution(object):
    def __init__(self):
        pass
    def solution(self, s):
        dic = {}
        ans = 0
        for _s in s:
            n = ord(_s)
            if n <= 127 and n >= 0:
                if _s in dic:
                    pass
                else:
                    ans += 1
                    dic[_s] = 1
            else:
                pass
        return ans

    
if __name__ == "__main__":
    while True:
        try:
            s = input().strip()
            slt = Solution()
            ans = slt.solution(s)
            print(ans)
        except EOFError:
            break
