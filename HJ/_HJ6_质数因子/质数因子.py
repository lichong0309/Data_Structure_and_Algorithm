import math
class Solution(object):
    def __init__(self):
        self.ans = []
    def solution(self, n):
        # 1. 如果n == 1
        if n == 1:
            self.ans.append(str(n))
            return self.ans
        # 2. 如果n >= 2
        else:
            i = 2
            # 从 2 开始寻找因子
            while i <= math.sqrt(n):
                # 2.1 如果n和i的模为0，则说明i为n的因子
                if n % i == 0:
                    n = int(n / i)              # 更新n
                    self.ans.append(str(i))     
                    i = 2                       # 复原i
                # 2.2: i继续遍历
                else:
                    i = i + 1   
            # 3. 如果最后留下一个质数
            if n != 1:
                self.ans.append(str(n))
            return self.ans
if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            slt = Solution()
            ans = slt.solution(n)
            print(' '.join(ans))
            
        except EOFError:
            break
