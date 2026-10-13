class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: x * x)
        i = 0
        j = len(nums) - 1
        s = 0

        while i <= j:
            s += (nums[j] * nums[j])
            if i != j:
                s -= (nums[i] * nums[i])
            i += 1
            j -= 1
        
        return s
