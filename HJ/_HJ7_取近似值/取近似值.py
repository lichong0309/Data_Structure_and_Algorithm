class Solution(object):
    def __init__(self):
        pass
    def solution(self, f):
        _f = f * 10
        n = _f % 10
        if n < 5:
            return int(f)
        else:
            return int(f) + 1
        

    
if __name__ == "__main__":
    while True:
        try:
            f = float(input().strip())
            slt = Solution()
            ans = slt.solution(f)
            print(ans)
        except EOFError:
            break
