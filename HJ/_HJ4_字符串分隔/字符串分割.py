class Solution(object):
    def __init__(self):
        self.ans = []
    def solution(self, s):
        if s == '':
            return self.ans.append('')
        else:
            n = len(s)
            if n <= 8:
                new_s = s + '0'*(8-n)
                self.ans.append(new_s)
            else:
                t = n // 8
                m = n % 8 
                # 1. 先处理整数部分
                for i in range(t):
                    self.ans.append(s[i*8:(i+1)*8])
                # 2. 在处理不能凑整的部分
                if m != 0:
                    self.ans.append(s[t*8:]+'0'*(8-m))
                else:
                    pass
        return self.ans

    
if __name__ == "__main__":
    while True:
        try:
            s = input().strip()
            so = Solution()
            ans = so.solution(s)
            # 依次输出ans中的字符串
            for _ans in ans:
                print(_ans)
        except EOFError:
            break
