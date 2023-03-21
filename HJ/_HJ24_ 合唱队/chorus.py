class Solution(object):
    def __init__(self):
        pass
    def solution(self, nums, n):
        # 思路：这种带有山峰类的题目，应该想到从左往右遍历一次加上从右往左遍历一次找到山峰的最高点。
        # 将最终保留的同学的身高从最高点分成两个部分，left部分和right的部分。
        # left部分
        leftdp = [0] * n 
        leftdp[0] = 1
        for i in range(1,n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    leftdp[i] = max(leftdp[i], leftdp[j])
                else:
                    pass
            leftdp[i] = leftdp[i] + 1

        # right部分
        rightdp = [0] * n
        rightdp[-1] = 1
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    rightdp[i] = max(rightdp[i], rightdp[j])
                else:
                    pass
            rightdp[i] = rightdp[i] + 1
        dp = [0] * n
        for i in range(n):
            dp[i] = leftdp[i] + rightdp[i] - 1
        total = max(dp)
        ans = n - total 
        return ans 


if __name__ == "__main__":
    while True:
        try:
            n = int(input().strip())
            nums = list(map(int,input().strip().split()))
            s = Solution()
            ans = s.solution(nums, n)
            print(ans)

        except EOFError:
            break