class Solution(object):
    def __init__(self):
        pass
    def solution(self, n):
        dic = {}
        ans = ''
        while n != 0:
            t = n % 10
            ans += str(t)
            n = n // 10
        return ans

    
if __name__ == "__main__":
    while True:
        try:
            n = int(input().strip())
            slt = Solution()
            ans = slt.solution(n)
            print(int(ans))
        except EOFError:
            break
