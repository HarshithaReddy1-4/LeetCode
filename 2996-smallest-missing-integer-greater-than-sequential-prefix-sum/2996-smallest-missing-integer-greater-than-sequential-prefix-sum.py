class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        j = 1
        ans = nums[0]

        while j < len(nums):
            if nums[j] != nums[j - 1] + 1:
                break
            ans += nums[j]
            j += 1
        
        nums = set(nums)

        while True:
            if ans not in nums:
                return ans
            ans += 1
        
        