class Solution(object):
    def __init__(self):
        pass
    def solution(self, s):
        return int(s, 16)

    
if __name__ == "__main__":
    while True:
        try:
            s = input().strip()
            slt = Solution()
            ans = slt.solution(s)
            print(ans)
        except EOFError:
            break
