class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 0
        j = 1

        while j < len(nums):
            if nums[j] != nums[j - 1] + 1:
                break
            j += 1
        
        ans = sum(nums[0: j])
        nums = set(nums)

        while True:
            if ans not in nums:
                return ans
            ans += 1
        
        