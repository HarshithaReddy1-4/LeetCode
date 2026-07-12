class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, 0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
        for i in range(len(nums)):
            if zero:
                nums[i] = 0
                zero -= 1
            elif one:
                nums[i] = 1
                one -= 1
            else:
                nums[i] = 2
        
        