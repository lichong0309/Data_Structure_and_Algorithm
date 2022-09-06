class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        for i in range(length-1, 0, -1):
            # 从后往前遍历，找到第一个不是升序的位置，为i-1
            if nums[i-1] < nums[i]:
                
                # 找到大于nums[i-1]最小的元素的位置，记为j
                for j in range(length-1, i-1, -1):
                    if nums[j] <= nums[i-1]:
                        pass
                    else:
                        # 交换位置
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break            # 退出循环
                print(nums)
                # 反转nums[i:]的所有元素
                subListLength = length - 1 - (i-1)
                for m in range(subListLength//2):
                    left = m + i
                    right = length - 1 - m
                    # 交换
                    nums[left], nums[right] = nums[right], nums[left]

                return 
            
            else:
                pass

        nums.reverse()
                

nums = [1,3,2]

s = Solution()
s.nextPermutation(nums)
print(nums)