class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 对nums进行升序排序,后续比较
        n = sorted(nums, reverse=False)
        length = len(nums)         # nums长度
        count = 0                  # 计数
        left = 0                   # 左指针
        right = length - 1         # 右指针
        
        # 左指针遍历
        while left <= right and left < length and nums[left]==n[left]:
            count = count + 1 
            left = left + 1

        # 右指针遍历
        while left < right and right > 0 and nums[right]==n[right]:
            count = count + 1
            right = right - 1 
            
        count = length - count 
        return count 


        

            