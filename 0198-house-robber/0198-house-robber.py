class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        prev1, prev2 = max(nums[0], nums[1]), nums[0]
        m = 0
        for i in range(2, n):
            m = max(nums[i] + prev2, prev1)
            prev1, prev2 = m, prev1
        return m
