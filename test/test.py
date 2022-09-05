class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # # 使用倒叙遍历相加的方法，时间复杂度O（n^2）
        # # 不适用倒叙遍历，从0号位置正序遍历，则时间复杂度为O（n^3),超时
        # length = len(nums)

        # ans = 0

        # # 遍历整个list，作为起始节点
        # for start in range(length):
        #     _sum = 0
        #     for end in range(start, -1, -1):            # 从start开始倒叙遍历
        #         _sum += nums[end]
        #         if _sum == k:
        #             ans += 1
        # return ans 

        # 使用前缀和 、 哈希表

        length = len(nums)
        ans = 0 
        dic = {}            # key:前缀和 value:前缀和出现的次数（因为可能相同的key出现在不同的位置，不能覆盖，但是只需要记录出现的次数即可）
        dic[0] = 1          # 初始化

        _sum = 0 
        for i in range(length):
            _sum += nums[i]
            # 将前缀和加入字典中
            if _sum in dic:
                dic[_sum] += 1
            else:
                dic[_sum] = 1


            remind = _sum - k            # 寻找符合条件的前缀和
            if remind in dic:
                ans += dic[remind]
            else:
                pass
                
        return ans 
                

nums = [-1,-1,1]
k = 0
s = Solution()
ans = s.subarraySum(nums, k)
print(ans)