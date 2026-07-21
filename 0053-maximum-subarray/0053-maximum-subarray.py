class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = nums[0]
        mx = curr
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            mx = max(mx, curr)

        return mx
