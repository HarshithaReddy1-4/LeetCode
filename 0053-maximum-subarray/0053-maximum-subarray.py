class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        mx = pref[0]
        for i in range(1, n):
            pref[i] = max(pref[i - 1] + nums[i], nums[i])
            mx = max(mx, pref[i])

        return mx
