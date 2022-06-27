'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# 灵感来源于 基数排序

class Solution:
    def reverse(self, x: int) -> int:

        if x >= -2 ** 31 and x <=2**31 -1:
            if x < 0:
                y = - x 
            else:
                y = x

            length = len(str(y))            # 得到长度
            count = 0                       # 结果值

            for i in range(length):
                remain = (y // (10 ** i)) % 10 
                if x < 0:
                    count = - remain * (10**(length-1-i)) + count        # 得到新值
                else:
                    count =   remain * (10**(length-1-i)) + count           

            if count >= -2 ** 31 and count <= 2**31 -1:
                return count
            else:
                return 0

        else:
            return 0 
        
