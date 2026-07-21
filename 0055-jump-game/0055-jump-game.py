class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] - 1 < 0:
                return False
            dp[i] = max(nums[i], dp[i - 1] - 1)
        return True